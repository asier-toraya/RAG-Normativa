# MVPs y Aproximaciones del Proyecto

## Resumen

Hasta ahora se han realizado dos aproximaciones simples para comprobar la viabilidad general del proyecto:

1. una aproximación con `n8n`;
2. una aproximación local en Python con Ollama y ChromaDB.

Ambas deben entenderse como MVPs o pruebas de concepto. Ninguna equivale todavía al sistema completo planteado en `Documentacion/informeIA.md`.

## Aproximación 1: experimento con `n8n`

La aproximación con `n8n` debe considerarse un experimento descartado en su estado actual.

Lo que sí quedó validado:

- Ollama respondía correctamente por HTTP;
- la conectividad básica desde otros puntos de la red funcionaba;
- era posible alcanzar el servicio y obtener respuestas del modelo.

Lo que no quedó resuelto:

- el cierre correcto del ciclo entrada-respuesta en los flujos;
- la interacción estable entre disparadores de chat y peticiones manuales;
- una base sólida para usar `n8n` como capa de orquestación del agente.

Conclusión práctica:

- `n8n` no ha quedado validado como base operativa del proyecto;
- el documento `Documentacion/intento-n8n.md` debe leerse como bitácora de intento fallido, no como descripción de la solución elegida.

## Aproximación 2: MVP local en Python

La aproximación local es la que hoy constituye el núcleo funcional del repositorio.

Lo que sí aporta:

- ejecución enteramente local;
- arquitectura simple;
- comportamiento reproducible;
- control directo del corpus;
- menor dependencia de herramientas externas;
- base razonable para evolucionar hacia la arquitectura futura.

Lo que todavía no aporta:

- una orquestación multiagente rica;
- varios especialistas jurídicos reales trabajando en paralelo;
- ingestión automática desde fuentes oficiales;
- una capa madura de herramientas externas;
- actualización normativa continua.

## Conclusión

La aproximación local es el MVP válido y operativo del proyecto en este momento.

La aproximación con `n8n` fue útil para descartar una vía de implementación temprana, pero no debe presentarse como prueba de que la arquitectura multiagente ya existe o funciona de extremo a extremo.

