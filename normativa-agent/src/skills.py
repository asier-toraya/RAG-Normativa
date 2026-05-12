from __future__ import annotations

from pathlib import Path


SKILLS_DIR = Path(__file__).resolve().parent.parent / "skills"


def load_skill(name: str) -> str:
    path = SKILLS_DIR / f"{name}.md"
    try:
        content = path.read_text(encoding="utf-8").strip()
    except FileNotFoundError as exc:
        raise RuntimeError(f"No se encontró la skill requerida: {path}") from exc

    if not content:
        raise RuntimeError(f"La skill está vacía: {path}")
    return content


def compose_skills(*names: str) -> str:
    return "\n\n".join(load_skill(name) for name in names)
