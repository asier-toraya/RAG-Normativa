# Sistema Agéntico Normativo

Este repositorio contiene dos planos distintos del proyecto y conviene leerlos por separado para evitar confusión:

1. La visión futura del sistema, descrita en [Documentacion/informeIA.md](Documentacion/informeIA.md).
2. El estado implementado hoy, documentado en [ESTADO-ACTUAL.md](ESTADO-ACTUAL.md).

`Documentacion/informeIA.md` debe considerarse el documento principal de diseño y la referencia correcta sobre la idea objetivo del proyecto. Describe la arquitectura deseada a medio plazo: sistema multiagente jurídico, subagentes especializados, actualización normativa, integración de herramientas y generación de informes estructurados.

El código existente en `normativa-agent/` no implementa todavía esa arquitectura completa. Lo que existe hoy es un MVP funcional local, mucho más simple, basado en:

- consulta RAG sobre corpus Markdown;
- Ollama como motor local;
- ChromaDB como base vectorial;
- un flujo secuencial con orquestador simple, agente de normativa y corrector opcional.

Para entender el repositorio sin mezclar planos, conviene seguir este orden:

1. [Documentacion/informeIA.md](Documentacion/informeIA.md)
2. [ESTADO-ACTUAL.md](ESTADO-ACTUAL.md)
3. [MVPS-Y-APROXIMACIONES.md](MVPS-Y-APROXIMACIONES.md)
4. [MAPA-DOCUMENTACION.md](MAPA-DOCUMENTACION.md)

## Regla de lectura recomendada

Si un documento entra en conflicto con `informeIA.md`, debe interpretarse así:

- `informeIA.md` fija la dirección futura del proyecto;
- los documentos del directorio `normativa-agent/` describen el MVP local real;
- los documentos de experimentación, como `intento-n8n.md`, describen pruebas y límites, no la arquitectura final.

## Estado resumido

Hoy el proyecto demuestra que la línea de trabajo es viable en local, pero no demuestra todavía la arquitectura multiagente completa definida en `informeIA.md`.

