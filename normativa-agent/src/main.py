from __future__ import annotations

from .agents import OrchestratorAgent
from .config import get_settings


EXIT_COMMANDS = {"salir", "exit", "quit"}


def main() -> None:
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
