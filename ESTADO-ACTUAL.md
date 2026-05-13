# Estado Actual del Proyecto

## Qué está implementado realmente

El estado actual del repositorio se concentra en `normativa-agent/` y corresponde a un MVP local de complejidad baja o media, no al sistema final descrito en `Documentacion/informeIA.md`.

Ese MVP implementa:

- una CLI local para lanzar consultas;
- un flujo RAG sobre documentos Markdown;
- embeddings con Ollama;
- almacenamiento vectorial en ChromaDB;
- un orquestador simple;
- un agente de normativa;
- un corrector opcional de estilo.

## Qué no está implementado todavía

A fecha del estado actual del repositorio, no existe todavía implementación profunda de:

- subagente de jurisprudencia;
- subagente de actualización normativa;
- resolución automática de conflictos entre agentes;
- procesamiento paralelo real entre subagentes;
- MCP operativo dentro del MVP local;
- Playwright integrado en el flujo del proyecto;
- `n8n` como orquestador funcional del sistema;
- `vLLM` o `LM Studio` integrados como backend real del código actual.

## Cómo debe interpretarse `informeIA.md`

`Documentacion/informeIA.md` es correcto como documento principal de visión futura. No debe leerse como descripción exacta del código actual, sino como especificación de la arquitectura objetivo.

En otras palabras:

- la idea del proyecto está bien definida en `informeIA.md`;
- el desarrollo real todavía está en fase temprana;
- los MVP existentes validan partes del enfoque, no el sistema completo.

## Qué valida el MVP local

El MVP local sí valida varios puntos importantes:

- que se puede consultar un corpus normativo local;
- que Ollama puede servir embeddings y generación;
- que ChromaDB puede sostener una recuperación local útil;
- que la separación básica entre recuperación, respuesta y corrección final es operativa;
- que el proyecto puede ejecutarse sin depender de servicios externos.

## Qué no valida el MVP local

No valida todavía:

- especialización jurídica real por subdominios;
- razonamiento cooperativo entre varios agentes fuertes;
- arbitraje entre salidas de agentes distintos;
- actualización automática del corpus desde fuentes oficiales;
- integración robusta de jurisprudencia;
- trazabilidad completa de una cadena multiagente compleja.

## Riesgo principal de interpretación

El mayor riesgo documental del repositorio era confundir la visión futura con el estado real. Este archivo existe precisamente para evitar esa lectura errónea.

