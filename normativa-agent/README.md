# Normativa Agent

Sistema multiagente local en Python para consultas sobre normativa de ciberseguridad usando Ollama, ChromaDB y documentos Markdown.

## Descripción

El proyecto implementa un patrón multiagente sencillo y defendible:

- Un agente orquestador recibe la consulta.
- Un subagente de normativa recupera fragmentos relevantes desde una base vectorial local y redacta una respuesta limitada al contenido recuperado.
- Un subagente corrector opcional mejora ortografía, claridad y formato sin alterar el significado técnico ni la sección de fuentes.

Todo el flujo funciona en local y evita frameworks multiagente complejos.

La documentación adicional está en:

- [Documentacion/mejoras-eficiencia.md](Documentacion/mejoras-eficiencia.md)
- [Documentacion/uso-y-operacion.md](Documentacion/uso-y-operacion.md)

## Arquitectura de agentes

```text
Usuario
  │
  ▼
Agente orquestador
  │
  ├─► Subagente de normativa
  │     ├─► Embedding de la consulta con Ollama
  │     ├─► Recuperación Top-K en ChromaDB
  │     └─► Respuesta con modelo de chat
  │
  └─► Subagente corrector opcional
        └─► Mejora de redacción sin cambiar el contenido técnico
```

## Estructura

```text
normativa-agent/
├── Documentacion/
│   ├── mejoras-eficiencia.md
│   └── uso-y-operacion.md
├── normativa/
│   └── ejemplo.md
├── src/
│   ├── __init__.py
│   ├── agents.py
│   ├── config.py
│   ├── ingest.py
│   ├── main.py
│   └── rag.py
├── db/
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Requisitos

- Python 3.11 o superior
- Ollama instalado y en ejecución
- Modelos locales descargados

Hardware objetivo recomendado:

- 12 GB de RAM
- NVIDIA RTX 2060 portátil

## Instalación

1. Crear y activar un entorno virtual:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Linux/macOS:

```bash
source .venv/bin/activate
```

2. Instalar dependencias:

```bash
pip install -r requirements.txt
```

3. Crear el archivo de configuración:

```bash
cp .env.example .env
```

En Windows PowerShell también puedes usar:

```powershell
Copy-Item .env.example .env
```

## Descarga de modelos Ollama

Modelos requeridos:

```bash
ollama pull qwen3:8b
ollama pull llama3.1:8b
ollama pull nomic-embed-text
```

## Configuración

Variables principales en `.env`:

- `CHAT_MODEL=qwen3:8b`
- `ALT_CHAT_MODEL=llama3.1:8b`
- `EMBED_MODEL=nomic-embed-text`
- `ENABLE_CORRECTOR=false`
- `OLLAMA_HOST=http://localhost:11434`
- `OLLAMA_MODELS=./ollama-models`
- `CHROMA_PATH=./db`
- `NORMATIVA_PATH=./normativa`
- `TOP_K=5`
- `CHUNK_SIZE=1200`
- `CHUNK_OVERLAP=150`
- `EMBED_BATCH_SIZE=32`
- `CHROMA_COLLECTION=normativa`

Notas:

- `ENABLE_CORRECTOR=false` reduce latencia porque evita una segunda llamada al modelo de chat.
- `EMBED_BATCH_SIZE` controla cuántos fragmentos se procesan por lote durante la ingesta.

## Indexación de documentos

Coloca tus ficheros Markdown dentro de `normativa/` y ejecuta:

```bash
python -m src.ingest
```

La ingesta:

- Lee todos los `.md`.
- Normaliza Markdown básico.
- Divide el contenido en fragmentos.
- Genera embeddings con `nomic-embed-text` por lotes.
- Actualiza solo los archivos nuevos o modificados.
- Elimina de ChromaDB los fragmentos de archivos que ya no existen.
- Guarda textos y metadatos en ChromaDB mediante sincronización incremental.

## Ejecución

Inicia la CLI interactiva con:

```bash
python -m src.main
```

Prompt esperado:

```text
Consulta normativa >
```

Comandos de salida:

- `salir`
- `exit`
- `quit`

Si ya había una terminal abierta con una versión anterior del proceso, reiníciala para que cargue la configuración y el código actualizados.

## Ejemplo de uso

Consulta:

```text
Consulta normativa > ¿Qué exige la normativa interna sobre la notificación de incidentes?
```

Respuesta esperada:

- Síntesis basada únicamente en fragmentos recuperados.
- Sección final `Fuentes consultadas`.

Si el corpus no contiene evidencia suficiente, el sistema responderá exactamente:

```text
No encuentro información suficiente en la normativa cargada.
```

## Cómo añadir nueva normativa

1. Copia nuevos archivos `.md` dentro de `normativa/`.
2. Ejecuta de nuevo:

```bash
python -m src.ingest
```

3. Inicia o reinicia la CLI:

```bash
python -m src.main
```

## Comandos habituales

```bash
pip install -r requirements.txt
ollama pull qwen3:8b
ollama pull nomic-embed-text
python -m src.ingest
python -m src.main
```

## Notas de diseño

- No se usan LangGraph, CrewAI, AutoGen ni otros frameworks complejos.
- El patrón multiagente está implementado manualmente con clases ligeras.
- El modelo principal puede cambiarse desde `.env`.
- La base vectorial es completamente local.
