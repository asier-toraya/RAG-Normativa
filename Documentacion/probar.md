# Cómo probar el proyecto manualmente

## Objetivo

Este documento explica cómo comprobar manualmente que el sistema está funcionando y cómo lanzar una consulta real sobre la normativa cargada.

## 1. Abrir una terminal en el proyecto

Sitúate en la carpeta del proyecto:

```powershell
cd C:\Proyectos\Normativa\SISTEMA-AGENTICO\normativa-agent
```

## 2. Arrancar Ollama con los modelos locales del proyecto

Ejecuta:

```powershell
cmd /c scripts\start_ollama_local.cmd
```

Qué debes comprobar:

- La consola de Ollama debe quedarse abierta.
- No debe mostrar errores críticos.
- Debe escuchar en `127.0.0.1:11434`.

## 3. Verificar que los modelos están disponibles

Abre otra terminal y ejecuta:

```powershell
cd C:\Proyectos\Normativa\SISTEMA-AGENTICO\normativa-agent
cmd /c "set OLLAMA_HOST=http://127.0.0.1:11434 && set OLLAMA_MODELS=C:\Proyectos\Normativa\SISTEMA-AGENTICO\normativa-agent\ollama-models && ollama list"
```

Debes ver estos modelos:

- `qwen3:8b`
- `llama3.1:8b`
- `nomic-embed-text`

## 4. Comprobar que la normativa está indexada

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m src.ingest
```

Qué debes comprobar:

- Debe aparecer `Leyendo normativa local...`
- Debe aparecer `Indexación completada`
- No debe aparecer un error de conexión con Ollama

## 5. Lanzar la aplicación interactiva

Ejecuta:

```powershell
.\.venv\Scripts\python.exe -m src.main
```

Debes ver:

```text
Consulta normativa >
```

## 6. Hacer una consulta mínima

Escribe esta consulta:

```text
¿En cuánto tiempo debe hacerse la notificación interna de un incidente de severidad alta o crítica?
```

Resultado esperado:

- El sistema debe responder que la notificación interna debe realizarse en un plazo máximo de dos horas desde la confirmación inicial.
- Debe mencionar las fuentes consultadas.

## 7. Probar un caso sin suficiente evidencia

Escribe esta consulta:

```text
¿Qué sanciones económicas prevé esta normativa?
```

Resultado esperado:

```text
No encuentro información suficiente en la normativa cargada.
```

## 8. Cómo salir

Dentro de la CLI puedes salir escribiendo:

- `salir`
- `exit`
- `quit`

## 9. Fallos habituales

### Ollama no responde

Comprueba que sigue abierta la terminal donde ejecutaste:

```powershell
cmd /c scripts\start_ollama_local.cmd
```

### No aparecen modelos en `ollama list`

Vuelve a descargar los modelos:

```powershell
cmd /c scripts\pull_models_local.cmd
```

### Falla la ingesta

Comprueba:

- que Ollama está activo,
- que existen archivos `.md` en `normativa/`,
- que el entorno virtual `.venv` existe.

### La respuesta tarda mucho

Es normal en la primera ejecución del modelo.
Ollama necesita cargar el modelo en memoria y preparar la inferencia.

