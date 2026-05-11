from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
from pathlib import Path
from typing import Iterable, Iterator

import chromadb
from chromadb.api.models.Collection import Collection
from ollama import Client, ResponseError

from .config import Settings, get_settings


INGEST_STATE_FILE = "ingest-state.json"
INGEST_STATE_VERSION = 1


@dataclass(slots=True)
class ChunkRecord:
    chunk_id: str
    text: str
    source: str
    chunk_index: int


@dataclass(slots=True)
class FileRecord:
    source: str
    content_hash: str
    chunks: list[ChunkRecord]


@dataclass(slots=True)
class IngestSummary:
    indexed_files: int
    indexed_chunks: int
    removed_files: int
    skipped_files: int
    full_rebuild: bool


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


def hash_content(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def build_file_record(file_path: Path, settings: Settings) -> FileRecord:
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

    return FileRecord(
        source=file_path.name,
        content_hash=hash_content(normalized_content),
        chunks=[
            ChunkRecord(
                chunk_id=f"{file_path.stem}-{chunk_index}",
                text=chunk,
                source=file_path.name,
                chunk_index=chunk_index,
            )
            for chunk_index, chunk in enumerate(chunks)
        ],
    )


def build_file_records(files: Iterable[Path], settings: Settings) -> list[FileRecord]:
    records = [build_file_record(file_path, settings) for file_path in files]
    if not any(record.chunks for record in records):
        raise ValueError("Los archivos Markdown existen, pero no generaron fragmentos indexables.")
    return records


def iter_batches(items: list[ChunkRecord], batch_size: int) -> Iterator[list[ChunkRecord]]:
    for index in range(0, len(items), batch_size):
        yield items[index:index + batch_size]


def get_ingest_state_path(settings: Settings) -> Path:
    return settings.chroma_path / INGEST_STATE_FILE


def load_ingest_state(settings: Settings) -> tuple[dict[str, str], bool]:
    state_path = get_ingest_state_path(settings)
    if not state_path.exists():
        return {}, False

    try:
        payload = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RuntimeError(f"No se ha podido leer el estado de ingesta: {exc}") from exc

    version = payload.get("version")
    files = payload.get("files")
    if version != INGEST_STATE_VERSION or not isinstance(files, dict):
        return {}, False

    return {str(key): str(value) for key, value in files.items()}, True


def save_ingest_state(settings: Settings, file_hashes: dict[str, str]) -> None:
    payload = {
        "version": INGEST_STATE_VERSION,
        "files": file_hashes,
    }
    get_ingest_state_path(settings).write_text(
        json.dumps(payload, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def flatten_chunks(records: Iterable[FileRecord]) -> list[ChunkRecord]:
    chunks: list[ChunkRecord] = []
    for record in records:
        chunks.extend(record.chunks)
    return chunks


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


def delete_sources(collection: Collection, sources: Iterable[str]) -> None:
    for source in sources:
        collection.delete(where={"source": source})


def ingest_documents(settings: Settings) -> IngestSummary:
    settings.chroma_path.mkdir(parents=True, exist_ok=True)

    files = load_markdown_files(settings.normativa_path)
    file_records = build_file_records(files, settings)
    current_hashes = {record.source: record.content_hash for record in file_records}
    previous_hashes, has_valid_state = load_ingest_state(settings)

    ollama_client = get_ollama_client(settings)
    chroma_client = chromadb.PersistentClient(path=str(settings.chroma_path))
    collection = chroma_client.get_or_create_collection(name=settings.chroma_collection)

    full_rebuild = not has_valid_state
    if not full_rebuild and collection.count() == 0 and previous_hashes:
        full_rebuild = True

    if full_rebuild:
        collection = reset_collection(chroma_client, settings.chroma_collection)
        changed_file_records = file_records
        removed_sources: list[str] = []
        skipped_files = 0
    else:
        changed_file_records = [
            record for record in file_records if previous_hashes.get(record.source) != record.content_hash
        ]
        removed_sources = sorted(set(previous_hashes) - set(current_hashes))
        delete_sources(
            collection,
            [record.source for record in changed_file_records] + removed_sources,
        )
        skipped_files = len(file_records) - len(changed_file_records)

    changed_chunks = flatten_chunks(changed_file_records)
    for batch in iter_batches(changed_chunks, settings.embed_batch_size):
        embeddings = embed_texts(
            client=ollama_client,
            model=settings.embed_model,
            texts=[record.text for record in batch],
        )
        collection.upsert(
            ids=[record.chunk_id for record in batch],
            documents=[record.text for record in batch],
            metadatas=[
                {"source": record.source, "chunk_index": record.chunk_index}
                for record in batch
            ],
            embeddings=embeddings,
        )

    save_ingest_state(settings, current_hashes)
    return IngestSummary(
        indexed_files=len(changed_file_records),
        indexed_chunks=len(changed_chunks),
        removed_files=len(removed_sources),
        skipped_files=skipped_files,
        full_rebuild=full_rebuild,
    )


def main() -> None:
    settings = get_settings()
    print("[ingest] Leyendo normativa local...")
    summary = ingest_documents(settings)
    print(
        "[ingest] Indexación completada. "
        f"Archivos indexados: {summary.indexed_files}. "
        f"Chunks actualizados: {summary.indexed_chunks}. "
        f"Archivos sin cambios: {summary.skipped_files}. "
        f"Archivos eliminados: {summary.removed_files}. "
        f"Reconstrucción completa: {'sí' if summary.full_rebuild else 'no'}."
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"[ingest] Error: {exc}")
        raise SystemExit(1) from exc
