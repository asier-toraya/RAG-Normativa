from __future__ import annotations

import sys

from .agents import OrchestratorAgent
from .config import get_settings


EXIT_COMMANDS = {"salir", "exit", "quit"}


def configure_stdio() -> None:
    for stream_name in ("stdin", "stdout", "stderr"):
        stream = getattr(sys, stream_name, None)
        if stream is None or not hasattr(stream, "reconfigure"):
            continue
        try:
            stream.reconfigure(encoding="utf-8")
        except Exception:
            continue


def main() -> None:
    configure_stdio()
    settings = get_settings()
    orchestrator = OrchestratorAgent(settings)

    print("Sistema multiagente de normativa listo.")
    print("Escribe tu consulta o usa salir, exit o quit para terminar.")

    while True:
        try:
            question = input("Consulta normativa > ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nSaliendo.")
            break

        if not question:
            continue

        if question.lower() in EXIT_COMMANDS:
            print("Saliendo.")
            break

        try:
            answer = orchestrator.run(question)
            print()
            print(answer)
            print()
        except Exception as exc:
            print(f"[error] {exc}")
            print()


if __name__ == "__main__":
    main()
