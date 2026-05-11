from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv
import os


load_dotenv()


@dataclass(slots=True)
class Settings:
    chat_model: str
    alt_chat_model: str
    embed_model: str
    ollama_host: str
    chroma_path: Path
    normativa_path: Path
    top_k: int
    chunk_size: int
    chunk_overlap: int
    chroma_collection: str


def get_settings() -> Settings:
    project_root = Path(__file__).resolve().parent.parent

    chunk_size = int(os.getenv("CHUNK_SIZE", "1200"))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", "150"))

    if chunk_overlap >= chunk_size:
        raise ValueError("CHUNK_OVERLAP debe ser menor que CHUNK_SIZE.")

    return Settings(
        chat_model=os.getenv("CHAT_MODEL", "qwen3:8b"),
        alt_chat_model=os.getenv("ALT_CHAT_MODEL", "llama3.1:8b"),
        embed_model=os.getenv("EMBED_MODEL", "nomic-embed-text"),
        ollama_host=os.getenv("OLLAMA_HOST", "http://localhost:11434"),
        chroma_path=(project_root / os.getenv("CHROMA_PATH", "./db")).resolve(),
        normativa_path=(project_root / os.getenv("NORMATIVA_PATH", "./normativa")).resolve(),
        top_k=int(os.getenv("TOP_K", "5")),
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        chroma_collection=os.getenv("CHROMA_COLLECTION", "normativa"),
    )

