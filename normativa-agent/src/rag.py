from __future__ import annotations

from dataclasses import dataclass

import chromadb
from chromadb.api.models.Collection import Collection
from ollama import Client, ResponseError

from .config import Settings


NO_INFO_RESPONSE = "No encuentro información suficiente en la normativa cargada."


@dataclass(slots=True)
class RetrievalResult:
    context: str
    sources: list[str]
    chunks: list[str]


class NormativaRAG:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.ollama_client = Client(host=settings.ollama_host)
        self.chroma_client = chromadb.PersistentClient(path=str(settings.chroma_path))
        self._collection: Collection | None = None

    def _get_collection(self) -> Collection:
        if self._collection is not None:
            return self._collection

        try:
            self._collection = self.chroma_client.get_collection(
                name=self.settings.chroma_collection
            )
        except Exception as exc:
            raise RuntimeError(
                "La base vectorial no está inicializada. Ejecuta primero `python -m src.ingest`."
            ) from exc

        return self._collection

    def _embed_query(self, question: str) -> list[float]:
        try:
            response = self.ollama_client.embed(model=self.settings.embed_model, input=question)
        except ResponseError as exc:
            raise RuntimeError(f"Error de Ollama al generar el embedding de consulta: {exc.error}") from exc
        except Exception as exc:
            raise RuntimeError(
                "No ha sido posible conectar con Ollama. Verifica que el servicio esté activo."
            ) from exc

        embeddings = response.get("embeddings")
        if not embeddings:
            raise RuntimeError("Ollama no devolvió embeddings para la consulta.")
        return embeddings[0]

    def retrieve(self, question: str) -> RetrievalResult:
        collection = self._get_collection()
        query_embedding = self._embed_query(question)
        result = collection.query(
            query_embeddings=[query_embedding],
            n_results=self.settings.top_k,
            include=["documents", "metadatas"],
        )

        documents = (result.get("documents") or [[]])[0]
        metadatas = (result.get("metadatas") or [[]])[0]

        if not documents:
            return RetrievalResult(context="", sources=[], chunks=[])

        sources: list[str] = []
        context_parts: list[str] = []

        for index, document in enumerate(documents):
            metadata = metadatas[index] if index < len(metadatas) else {}
            source = str(metadata.get("source", "desconocido.md"))
            chunk_index = metadata.get("chunk_index", "?")
            if source not in sources:
                sources.append(source)
            context_parts.append(f"[Fuente: {source} | chunk: {chunk_index}]\n{document}")

        return RetrievalResult(
            context="\n\n".join(context_parts),
            sources=sources,
            chunks=documents,
        )

    def answer_with_context(self, question: str, retrieval: RetrievalResult) -> str:
        if not retrieval.context.strip():
            return NO_INFO_RESPONSE

        messages = [
            {
                "role": "system",
                "content": (
                    "Eres un subagente de normativa. Responde exclusivamente con la "
                    "información presente en el contexto recuperado. No añadas conocimiento "
                    "externo, no inventes obligaciones y no cites fuentes no incluidas. "
                    "Si el contexto no basta para responder, devuelve exactamente: "
                    f"{NO_INFO_RESPONSE}"
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Pregunta del usuario:\n{question}\n\n"
                    f"Contexto recuperado:\n{retrieval.context}\n\n"
                    "Redacta una respuesta clara y técnica en español. "
                    "Incluye al final una sección titulada 'Fuentes consultadas' "
                    "con una lista simple de los nombres de archivo usados."
                ),
            },
        ]

        try:
            response = self.ollama_client.chat(
                model=self.settings.chat_model,
                messages=messages,
                options={"temperature": 0.1},
            )
        except ResponseError as exc:
            raise RuntimeError(f"Error de Ollama al generar la respuesta: {exc.error}") from exc
        except Exception as exc:
            raise RuntimeError(
                "No ha sido posible conectar con Ollama. Verifica que el servicio esté activo."
            ) from exc

        content = response["message"]["content"].strip()
        if not content:
            return NO_INFO_RESPONSE
        if content == NO_INFO_RESPONSE:
            return content

        if "Fuentes consultadas" not in content:
            sources_block = "\n".join(f"- {source}" for source in retrieval.sources)
            content = f"{content}\n\nFuentes consultadas\n{sources_block}"

        return content
