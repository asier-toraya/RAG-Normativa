# Skills del proyecto

Esta carpeta define las `skills` internas de `normativa-agent`.

En este proyecto, una `skill` no es un framework externo ni un agente nuevo por sí mismo. Es un documento de comportamiento que fija el contrato operativo de cada agente o política del sistema:

- objetivo
- entradas y salidas
- límites
- criterio de rechazo
- formato esperado
- reglas de evidencia y citas

## Objetivo

Separar las políticas del sistema del código Python. El código ejecuta el flujo y estas `skills` describen cómo debe comportarse cada parte.

## Skills actuales

- `orchestrator.md`: rol del agente orquestador.
- `normativa.md`: contrato principal del agente de normativa.
- `corrector.md`: reglas del corrector opcional.
- `evidencia.md`: política de suficiencia de evidencia.
- `citas.md`: política de uso de fuentes y trazabilidad.

## Uso actual

El código carga estas `skills` para construir los mensajes de sistema de los agentes que usan modelo:

- `NormativaAgent` / `NormativaRAG`
- `CorrectorAgent`

El documento del orquestador queda como especificación funcional para evolución futura, aunque hoy el orquestador no usa un prompt propio.

## Regla de arquitectura

Antes de crear un agente nuevo, conviene preguntarse si el cambio es:

1. una mejora de comportamiento de un agente existente
2. una política reusable
3. una responsabilidad nueva que de verdad necesita lógica separada

Si es 1 o 2, primero debe resolverse aquí, en `skills/`.
