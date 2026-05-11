# Uso y Operación

## Objetivo

Este documento resume cómo arrancar, reiniciar y operar el sistema en local de forma práctica.

## Requisitos previos

Antes de usar la CLI, deben estar disponibles estos elementos:

- Entorno virtual creado en `.venv`.
- Dependencias instaladas desde `requirements.txt`.
- Ollama instalado.
- Modelos descargados.
- Corpus Markdown disponible en `normativa/`.

## Arranque inicial

### 1. Activar el entorno virtual

En PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

## 2. Iniciar Ollama

Si Ollama no está ya en ejecución:

```powershell
ollama serve
```

Si el proyecto usa los modelos locales del directorio `ollama-models`, conviene arrancarlo con la configuración del proyecto:

```powershell
$env:OLLAMA_HOST="http://127.0.0.1:11434"
$env:OLLAMA_MODELS="./ollama-models"
ollama serve
```

## 3. Verificar modelos disponibles

```powershell
ollama list
```

Deben existir al menos:

- `qwen3:8b`
- `llama3.1:8b`
- `nomic-embed-text`

## 4. Ejecutar la ingesta

```powershell
python -m src.ingest
```

Comportamiento esperado:

- En la primera ejecución puede hacer reconstrucción completa.
- En ejecuciones posteriores solo reindexa archivos nuevos o modificados.

## 5. Lanzar la CLI

```powershell
python -m src.main
```

Prompt esperado:

```text
Consulta normativa >
```

## Uso diario

Flujo normal:

1. Arrancar Ollama si no está activo.
2. Ejecutar `python -m src.ingest` si ha cambiado la carpeta `normativa/`.
3. Ejecutar `python -m src.main`.
4. Realizar consultas.

## Reinicio del sistema

Conviene reiniciar la CLI en estos casos:

- Se ha cambiado código en `src/`.
- Se ha modificado `.env`.
- Se ha actualizado el corpus y se quiere asegurar un estado limpio.

Pasos:

1. Cerrar la CLI con `salir`, `exit` o `quit`.
2. Volver a ejecutar `python -m src.ingest` si ha cambiado la normativa.
3. Lanzar de nuevo `python -m src.main`.

## Variables relevantes de operación

- `ENABLE_CORRECTOR=false`
  Desactiva el corrector para reducir latencia.

- `EMBED_BATCH_SIZE=32`
  Controla el tamaño del lote de embeddings en la ingesta.

- `TOP_K=5`
  Número máximo de fragmentos recuperados en consulta.

- `OLLAMA_HOST`
  Dirección del servicio Ollama.

- `CHROMA_PATH=./db`
  Ruta de la base vectorial local.

- `NORMATIVA_PATH=./normativa`
  Ruta del corpus Markdown.

## Comprobaciones rápidas

### Verificar que Ollama responde

```powershell
Invoke-WebRequest -UseBasicParsing http://127.0.0.1:11434/api/tags
```

## Verificar que la ingesta incremental funciona

Ejecuta dos veces:

```powershell
python -m src.ingest
```

Resultado esperado:

- La primera vez puede actualizar archivos y chunks.
- La segunda vez, si no hubo cambios, debe indicar `Archivos indexados: 0`.

## Problemas habituales

### La CLI no responde o falla al consultar

Revisar:

- Que Ollama siga activo.
- Que el modelo de chat exista.
- Que el embedding model exista.
- Que la base vectorial haya sido inicializada con `python -m src.ingest`.

## La respuesta tarda demasiado

Revisar:

- Si `ENABLE_CORRECTOR` está activado.
- Si Ollama está cargando un modelo grande por primera vez.
- Si la máquina está limitada de RAM o GPU.

## La ingesta no detecta cambios

Revisar:

- Que los archivos modificados estén dentro de `normativa/`.
- Que los archivos tengan extensión `.md`.
- Que `db/ingest-state.json` corresponda al corpus actual.

## Ficheros operativos importantes

- `src/main.py`
- `src/ingest.py`
- `src/config.py`
- `db/ingest-state.json`
- `.env`
- `.env.example`

## Recomendación práctica

Para trabajar de forma estable:

- Mantén Ollama en una terminal separada.
- Usa otra terminal para la CLI.
- Ejecuta la ingesta solo cuando cambie el corpus.
