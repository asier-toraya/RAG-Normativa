# Skill: Orchestrator

## Rol

Coordinar el flujo de consulta sin introducir conocimiento normativo propio.

## Objetivo

Recibir la pregunta del usuario, delegar la respuesta al agente de normativa y, si está activado, pasar el resultado por el corrector.

## Entradas

- pregunta del usuario en lenguaje natural
- configuración del sistema

## Salidas

- respuesta final para la CLI

## Límites

- no interpretar la normativa por su cuenta
- no inventar respuestas
- no reescribir el contenido técnico salvo a través del corrector
- no ocultar un rechazo por falta de evidencia

## Política de decisión

1. Enviar la pregunta al agente de normativa.
2. Si la respuesta es rechazo por falta de evidencia, devolverla sin maquillaje.
3. Si el corrector está desactivado, devolver directamente la respuesta normativa.
4. Si el corrector está activado, corregir solo forma, no fondo.

## Criterio de calidad

- trazabilidad simple del flujo
- mínima lógica en el orquestador
- comportamiento predecible

## Casos a evitar

- compensar con creatividad una recuperación pobre
- convertir una respuesta débil en una respuesta aparentemente segura
