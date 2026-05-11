from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import chromadb
from chromadb.api.models.Collection import Collection
from ollama import Client, ResponseError

from .config import Settings, get_settings


@dataclass(slots=True)
class ChunkRecord:
    chunk_id: str
    text: str
    source: str
    chunk_index: int


def normalize_markdown(content: str) -> str:
    normalized = content.replace("\r\n", "\n").replace("\r", "\n")
    normalized = "\n".join(line.rstrip() for line in normalized.split("\n"))
    while "\n\n\n" in normalized:
        normalized = normalized.replace("\n\n\n", "\n\n")
    return normalized.strip()


def chunk_text(text: str, chunk_size: int, overlap: int) -> list[str]:
    if not text:
        return []

    chunks: list[str] = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = text[start:end].strip()
        if chunk:
            chunks.append(chunk)
        if end >= text_length:
            break
        start = max(end - overlap, start + 1)

    return chunks


def load_markdown_files(normativa_path: Path) -> list[Path]:
    if not normativa_path.exists():
        raise FileNotFoundError(f"No existe la carpeta de normativa: {normativa_path}")

    files = sorted(normativa_path.glob("*.md"))
    if not files:
        raise FileNotFoundError(
            f"No se han encontrado archivos .md en la carpeta: {normativa_path}"
        )
    return files


def build_chunk_records(files: Iterable[Path], settings: Settings) -> list[ChunkRecord]:
    records: list[ChunkRecord] = []

    for file_path in files:
        try:
            raw_content = file_path.read_text(encoding="utf-8")
        except OSError as exc:
            raise OSError(f"Error al leer el archivo {file_path.name}: {exc}") from exc

        normalized_content = normalize_markdown(raw_content)
        chunks = chunk_text(
            normalized_content,
            chunk_size=settings.chunk_size,
            overlap=settings.chunk_overlap,
        )

        for chunk_index, chunk in enumerate(chunks):
            records.append(
                ChunkRecord(
                    chunk_id=f"{file_path.stem}-{chunk_index}",
                    text=chunk,
                    source=file_path.name,
                    chunk_index=chunk_index,
                )
            )

    if not records:
        raise ValueError("Los archivos Markdown existen, pero no generaron fragmentos indexables.")

    return records


def get_ollama_client(settings: Settings) -> Client:
    return Client(host=settings.ollama_host)


def embed_texts(client: Client, model: str, texts: list[str]) -> list[list[float]]:
    try:
        response = client.embed(model=model, input=texts)
    except ResponseError as exc:
        raise RuntimeError(f"Error de Ollama al generar embeddings: {exc.error}") from exc
    except Exception as exc:
        raise RuntimeError(
            "No ha sido posible conectar con Ollama. Verifica que el servicio esté activo."
        ) from exc

    embeddings = response.get("embeddings")
    if not embeddings:
        raise RuntimeError("Ollama no devolvió embeddings válidos.")
    return embeddings


def reset_collection(client: chromadb.PersistentClient, collection_name: str) -> Collection:
    try:
        client.delete_collection(name=collection_name)
    except Exception:
        pass
    return client.get_or_create_collection(name=collection_name)


def ingest_documents(settings: Settings) -> int:
    settings.chroma_path.mkdir(parents=True, exist_ok=True)

    files = load_markdown_files(settings.normativa_path)
    records = build_chunk_records(files, settings)

    ollama_client = get_ollama_client(settings)
    embeddings = embed_texts(
        client=ollama_client,
        model=settings.embed_model,
        texts=[record.text for record in records],
    )

    chroma_client = chromadb.PersistentClient(path=str(settings.chroma_path))
    collection = reset_collection(chroma_client, settings.chroma_collection)

    collection.add(
        ids=[record.chunk_id for record in records],
        documents=[record.text for record in records],
        metadatas=[
            {"source": record.source, "chunk_index": record.chunk_index} for record in records
        ],
        embeddings=embeddings,
    )

    return len(records)


def main() -> None:
    settings = get_settings()
    print("[ingest] Leyendo normativa local...")
    total_chunks = ingest_documents(settings)
    print(f"[ingest] Indexación completada. Chunks almacenados: {total_chunks}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[ingest] Error: {exc}")
        raise SystemExit(1) from exc

