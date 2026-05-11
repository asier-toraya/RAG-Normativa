# Mejoras de Eficiencia Implementadas

## Objetivo

Este documento resume las optimizaciones aplicadas al proyecto para reducir latencia en consulta, evitar trabajo redundante en la recuperación y hacer la ingesta más escalable.

## Cambios aplicados

### 1. Corrector opcional

Se ha añadido la variable `ENABLE_CORRECTOR`, con valor por defecto `false`.

Impacto:

- Evita una segunda llamada al modelo de chat en cada consulta.
- Reduce tiempo de respuesta y consumo de recursos.
- Mantiene la posibilidad de activar el corrector cuando interese priorizar presentación sobre latencia.

## 2. Optimización del camino de consulta

Se han aplicado dos ajustes en el componente RAG:

- La colección de Chroma se resuelve una vez y queda cacheada en memoria.
- Se ha eliminado la llamada a `count()` en cada consulta.

Impacto:

- Menos operaciones por petición.
- Menor sobrecarga en el camino caliente de ejecución.
- Menos latencia acumulada cuando el sistema se usa de forma repetida.

## 3. Limpieza de la consulta a Chroma

La recuperación ya no solicita `distances`, porque el proyecto no las usaba en la respuesta final.

Impacto:

- Menos datos devueltos por consulta.
- Menor trabajo innecesario en la capa de recuperación.

## 4. Embeddings por lotes

La ingesta ahora usa `EMBED_BATCH_SIZE` para procesar fragmentos en bloques.

Impacto:

- Reduce picos de memoria frente a una generación masiva de embeddings.
- Mejora la estabilidad cuando el corpus crezca.
- Permite ajustar el tamaño del lote según la máquina disponible.

## 5. Ingesta incremental por hash

La ingesta mantiene un estado local en `db/ingest-state.json` con el hash de cada archivo procesado.

Comportamiento:

- Si un archivo no cambia, no se vuelve a fragmentar ni a vectorizar.
- Si un archivo cambia, se eliminan sus fragmentos anteriores y se hace `upsert` de los nuevos.
- Si un archivo desaparece del corpus, sus fragmentos se eliminan de ChromaDB.
- Si no existe estado previo válido, el sistema hace una reconstrucción completa una sola vez.

Impacto:

- Evita reindexaciones completas innecesarias.
- Reduce drásticamente el tiempo de ingesta en iteraciones normales.
- Hace que el mantenimiento del corpus sea mucho más práctico.

## Variables nuevas o relevantes

- `ENABLE_CORRECTOR=false`
- `EMBED_BATCH_SIZE=32`

## Validación realizada

Se ha verificado lo siguiente:

- Compilación correcta de `src` con `python -m compileall src`.
- Primera ingesta con reconstrucción completa.
- Segunda ingesta sin cambios, confirmando el camino incremental.
- Consulta real con `ENABLE_CORRECTOR=false`.

## Limitaciones y observaciones

- Si `TOP_K` es mayor que el número real de fragmentos indexados, Chroma ajusta internamente el valor y puede mostrar un aviso informativo.
- La terminal interactiva debe reiniciarse tras cambios de código o configuración para cargar la versión nueva.

## Siguiente mejora razonable

La siguiente optimización útil sería revisar el algoritmo de fragmentación para pasar de un corte por caracteres a una división más orientada a párrafos o secciones, lo que podría mejorar precisión de recuperación y permitir reducir `TOP_K`.
