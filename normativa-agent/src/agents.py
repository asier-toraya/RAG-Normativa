from __future__ import annotations

from dataclasses import dataclass

from ollama import Client, ResponseError

from .config import Settings
from .rag import NO_INFO_RESPONSE, NormativaRAG, format_ollama_exception
from .skills import load_skill


@dataclass(slots=True)
class NormativaAgent:
    rag: NormativaRAG

    def run(self, question: str) -> str:
        load_skill("normativa")
        load_skill("evidencia")
        load_skill("citas")
        retrieval = self.rag.retrieve(question)
        return self.rag.answer_with_context(question, retrieval)


class CorrectorAgent:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.ollama_client = Client(host=settings.ollama_host)

    def _split_sources(self, answer: str) -> tuple[str, str]:
        marker = "Fuentes consultadas"
        if marker not in answer:
            return answer.strip(), ""

        body, sources = answer.split(marker, maxsplit=1)
        normalized_sources = f"{marker}{sources}".strip()
        return body.strip(), normalized_sources

    def run(self, answer: str) -> str:
        if answer.strip() == NO_INFO_RESPONSE:
            return NO_INFO_RESPONSE

        corrector_skill = load_skill("corrector")
        body, sources = self._split_sources(answer)
        if not body:
            return answer.strip()

        messages = [
            {
                "role": "system",
                "content": f"{corrector_skill}\n\nDevuelve solo el texto corregido.",
            },
            {
                "role": "user",
                "content": body,
            },
        ]

        try:
            response = self.ollama_client.chat(
                model=self.settings.chat_model,
                messages=messages,
                options={"temperature": 0.1},
            )
        except ResponseError as exc:
            raise RuntimeError(f"Error de Ollama al corregir la respuesta: {exc.error}") from exc
        except Exception as exc:
            raise RuntimeError(format_ollama_exception(exc)) from exc

        corrected_body = response["message"]["content"].strip() or body
        if not sources:
            return corrected_body
        return f"{corrected_body}\n\n{sources}".strip()


class OrchestratorAgent:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        self.normativa_agent = NormativaAgent(rag=NormativaRAG(settings))
        self.corrector_agent = CorrectorAgent(settings) if settings.enable_corrector else None

    def run(self, question: str) -> str:
        load_skill("orchestrator")
        print("[orchestrator] Ejecutando subagente de normativa...")
        normative_answer = self.normativa_agent.run(question)

        if self.corrector_agent is None:
            return normative_answer

        print("[orchestrator] Ejecutando subagente corrector...")
        final_answer = self.corrector_agent.run(normative_answer)
        return final_answer
