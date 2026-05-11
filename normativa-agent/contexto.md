# Contexto del Proyecto

## Qué es este proyecto

`normativa-agent` es un sistema multiagente local en Python para consultar normativa de ciberseguridad a partir de documentos Markdown.

El objetivo del proyecto es responder preguntas usando únicamente el contenido del corpus cargado, sin añadir conocimiento externo. La arquitectura está pensada para ser sencilla, local y defendible en un contexto académico o técnico.

## Tecnologías principales

- Python
- Ollama
- ChromaDB
- Documentos Markdown como corpus

Dependencias principales en `requirements.txt`:

- `chromadb`
- `ollama`
- `python-dotenv`

## Arquitectura funcional

El sistema tiene tres piezas principales:

1. `src/main.py`
   Lanza la CLI interactiva.

2. `src/agents.py`
   Define el orquestador, el agente de normativa y el corrector opcional.

3. `src/rag.py`
   Gestiona la recuperación de contexto en ChromaDB y la generación de la respuesta con el modelo de chat.

4. `src/ingest.py`
   Indexa los documentos Markdown en la base vectorial local.

## Flujo de consulta

1. El usuario escribe una pregunta en la CLI.
2. El orquestador llama al componente RAG.
3. El sistema genera el embedding de la consulta.
4. ChromaDB recupera los fragmentos más relevantes del corpus.
5. El modelo de chat redacta una respuesta basada solo en ese contexto.
6. Si está activado, el corrector hace una segunda pasada de estilo.

## Estado actual del proyecto

El proyecto está funcional y ya fue optimizado respecto a su versión inicial.

Mejoras implementadas:

- Corrector opcional mediante `ENABLE_CORRECTOR=false` por defecto.
- Caché de la colección de Chroma en memoria.
- Eliminación de `count()` en cada consulta.
- Eliminación de `distances` del `include` en la query.
- Ingesta por lotes con `EMBED_BATCH_SIZE`.
- Ingesta incremental por hash de archivo.
- Eliminación de fragmentos de archivos borrados del corpus.
- Persistencia del estado de ingesta en `db/ingest-state.json`.
- Documentación técnica y operativa añadida y corregida en UTF-8.

## Variables de configuración relevantes

El archivo `.env` controla la configuración. Variables importantes:

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

## Estructura importante del repositorio

- `src/`
  Código principal.

- `normativa/`
  Corpus Markdown que se indexa y consulta.

- `db/`
  Base vectorial local de ChromaDB y estado de ingesta.

- `ollama-models/`
  Modelos locales usados por Ollama en este proyecto.

- `Documentacion/`
  Documentación adicional del proyecto.

## Documentación ya creada

Ficheros importantes para entender el estado actual:

- `README.md`
  Visión general, instalación, configuración y uso.

- `Documentacion/mejoras-eficiencia.md`
  Explica las optimizaciones implementadas.

- `Documentacion/uso-y-operacion.md`
  Explica cómo arrancar, reiniciar y operar el sistema.

## Cómo arrancar el proyecto

1. Activar el entorno virtual:

```powershell
.venv\Scripts\Activate.ps1
```

2. Asegurarse de que Ollama está activo:

```powershell
ollama serve
```

3. Ejecutar la ingesta si ha cambiado el corpus:

```powershell
python -m src.ingest
```

4. Lanzar la CLI:

```powershell
python -m src.main
```

## Estado operativo conocido

- Ollama ya se ha usado con éxito en `http://127.0.0.1:11434`.
- Los modelos locales disponibles incluyen:
  - `qwen3:8b`
  - `llama3.1:8b`
  - `nomic-embed-text`
- La ingesta incremental se verificó correctamente:
  - Primera ejecución: reconstrucción completa.
  - Segunda ejecución: sin reindexación si no hay cambios.
- La consulta real también se probó correctamente con el corrector desactivado.

## Decisiones importantes ya tomadas

- No usar frameworks multiagente complejos como LangGraph, CrewAI o AutoGen.
- Mantener una arquitectura simple y manual.
- Priorizar ejecución local.
- Responder solo con evidencia del corpus.
- Dejar el corrector desactivado por defecto para reducir latencia.
- Mantener la documentación en castellano correcto y UTF-8.

## Limitaciones actuales

- El chunking sigue siendo por caracteres, no por párrafos o secciones.
- Si `TOP_K` es mayor que el número real de fragmentos indexados, Chroma puede mostrar un aviso informativo.
- La terminal interactiva debe reiniciarse tras cambios de código o configuración.

## Siguiente mejora razonable

La mejora técnica más lógica a continuación sería cambiar el algoritmo de fragmentación para que trabaje por estructura semántica o por párrafos en vez de hacerlo solo por longitud de caracteres.

## Qué conviene leer primero en otro chat

Si este proyecto se retoma en otro chat, conviene revisar en este orden:

1. `contexto.md`
2. `README.md`
3. `Documentacion/mejoras-eficiencia.md`
4. `Documentacion/uso-y-operacion.md`
5. `src/config.py`
6. `src/ingest.py`
7. `src/rag.py`
8. `src/agents.py`

## Resumen corto

Este proyecto es un asistente local de consulta normativa basado en RAG con Ollama y ChromaDB. Ya tiene mejoras de eficiencia implementadas, documentación actualizada y un flujo operativo validado para ingesta incremental y consulta interactiva.
