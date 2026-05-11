# Informe del proyecto

## Objetivo

Este proyecto implementa un sistema multiagente local en Python para responder consultas sobre normativa de ciberseguridad usando Ollama, ChromaDB y archivos Markdown.

Su finalidad es ofrecer un flujo sencillo, explicable y ejecutable en un equipo doméstico o académico, sin depender de servicios externos ni de frameworks multiagente complejos.

## Estructura principal

```text
normativa-agent/
├── normativa/        # Documentos Markdown que forman el corpus
├── src/              # Lógica del sistema
├── db/               # Base vectorial local de ChromaDB
├── ollama-models/    # Modelos descargados por Ollama
├── scripts/          # Scripts auxiliares para Windows
├── README.md
├── informe.md
└── requirements.txt
```

## Componentes

### 1. Agente orquestador

Está implementado en `src/agents.py`.
Recibe la pregunta del usuario y coordina dos pasos:

1. Ejecuta el subagente de normativa.
2. Ejecuta el subagente corrector.

Devuelve al usuario la respuesta final ya revisada.

### 2. Subagente de normativa

Usa RAG sobre el corpus local.
Su función es:

1. Generar el embedding de la consulta con `nomic-embed-text`.
2. Recuperar los fragmentos más relevantes desde ChromaDB.
3. Construir un contexto con esos fragmentos.
4. Pedir una respuesta al modelo `qwen3:8b`.
5. Limitar la respuesta al contenido recuperado.

Si el contexto no basta, devuelve exactamente:

```text
No encuentro información suficiente en la normativa cargada.
```

### 3. Subagente corrector

También está en `src/agents.py`.
Recibe la respuesta del subagente de normativa y mejora:

- ortografía,
- claridad,
- formato.

No debe añadir contenido nuevo ni alterar el sentido técnico.

## Flujo de trabajo

### Ingesta

La ingesta se implementa en `src/ingest.py`.
El proceso hace lo siguiente:

1. Lee todos los `.md` de la carpeta `normativa/`.
2. Normaliza el Markdown de forma básica.
3. Divide cada documento en fragmentos.
4. Genera embeddings con Ollama.
5. Guarda textos, embeddings y metadatos en ChromaDB.

Metadatos mínimos almacenados:

- `source`
- `chunk_index`

### Consulta

La consulta se lanza desde `src/main.py` mediante una CLI interactiva.
El flujo completo es:

1. El usuario escribe una pregunta.
2. El orquestador llama al subagente de normativa.
3. El subagente recupera contexto y genera una respuesta.
4. El orquestador llama al subagente corrector.
5. Se muestra la respuesta final en consola.

## Modelos utilizados

El proyecto está configurado para trabajar con:

- `qwen3:8b` como modelo principal de chat.
- `llama3.1:8b` como modelo alternativo configurable.
- `nomic-embed-text` para embeddings.

Todos se ejecutan en local mediante Ollama.

## Configuración

La configuración se centraliza en `.env` y en `src/config.py`.
Variables principales:

- `CHAT_MODEL`
- `ALT_CHAT_MODEL`
- `EMBED_MODEL`
- `OLLAMA_HOST`
- `OLLAMA_MODELS`
- `CHROMA_PATH`
- `NORMATIVA_PATH`
- `TOP_K`
- `CHUNK_SIZE`
- `CHUNK_OVERLAP`

## Ejecución básica

### 1. Arranque de Ollama

En este proyecto se usa un almacén local de modelos dentro de `ollama-models/`, para evitar problemas de permisos en el perfil del usuario.

Script recomendado:

```powershell
cmd /c scripts\start_ollama_local.cmd
```

### 2. Indexación del corpus

```powershell
.\.venv\Scripts\python.exe -m src.ingest
```

### 3. Lanzamiento de la CLI

```powershell
.\.venv\Scripts\python.exe -m src.main
```

## Ventajas del diseño

- Todo funciona en local.
- La arquitectura es simple y defendible.
- El patrón multiagente está implementado manualmente.
- El corpus puede ampliarse añadiendo nuevos archivos Markdown.
- El sistema separa recuperación, generación y corrección final.

## Limitaciones

- La calidad de la respuesta depende del corpus cargado.
- Si la normativa es escasa, la respuesta puede ser insuficiente.
- La primera carga de modelos puede tardar varios minutos.
- El rendimiento depende de la RAM, la GPU disponible y el tamaño del modelo.

## Estado actual

El entorno quedó preparado y validado con:

- dependencias instaladas en `.venv`,
- modelos descargados en `ollama-models/`,
- ingesta completada,
- consulta de extremo a extremo probada con éxito sobre `normativa/ejemplo.md`.

