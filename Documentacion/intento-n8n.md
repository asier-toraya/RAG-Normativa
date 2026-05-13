
# Informe Técnico: Evaluación y Desistimiento de Implementación en n8n

## 1. Resumen de la Situación

Se intentó desarrollar una arquitectura de IA agéntica utilizando **n8n** y **Ollama** como motor de inferencia local. Tras validar que el servidor Ollama funciona correctamente de forma independiente y con modelos ligeros, se identificaron fallos críticos en la gestión de datos dentro de los flujos de n8n que impidieron la implementación.

## 2. Pruebas Realizadas y Hallazgos

### A. Validación del Motor de Inferencia (Ollama)

* **Acción:** Se realizaron pruebas con modelos ligeros (`qwen3.5:0.8b`), llamadas directas vía **HTTP Request**.
* **Resultado:** **Exitoso.** Se comprobó que Ollama procesa las peticiones sin errores de hardware ni de memoria, respondiendo de forma fluida.
![http_request](/Documentacion/IMG/http_request.jpg)

### B. Validación del Motor de Inferencia (Ollama)

* **Acción:** Se comprobo el acceso a Ollama desde dispositivos externos y en n8n.
* **Resultado:** **Exitoso.** Se comprobó que Ollama procesa las peticiones externas sin problemas.
![check_ollama_on_another_device](/Documentacion/IMG/check_ollama_on_another_device.jpeg)
En otro Dispositivo  
![](/Documentacion/IMG/n8n_connected_ollama.jpg)
Desde n8n

### C. Implementación con Nodos Nativos (Ollama Node)

* **Acción:** Se intentó configurar el nodo base de Ollama integrado en n8n.
* **Resultado:** Fallo persistente. El nodo no lograba establecer una comunicación estable para la ejecución del agente, devolviendo mensajes de error genéricos a pesar de que el servicio de Ollama estaba accesible.
![n8n_ollama_node](/Documentacion/IMG/n8n_ollama_node.jpg)
Configuracion usada  
![chat_error](/Documentacion/IMG/chat_error.jpg)  
Error Generado  

### D. Integración de HTTP Request

* **Acción:** Ante el fallo del nodo nativo, se intentó construir un flujo manual usando  **HTTP Request**.
* **Problema:** n8n consigue hacer peticiones a Ollama con respuestas válidas.
![n8n_http_request](/Documentacion/IMG/n8n_http_request.jpg)

### D. Fallo de Integración Chat Trigger + HTTP Request

* **Acción:** Ante el fallo del nodo nativo, se intentó construir un flujo manual usando **Chat Trigger** y **HTTP Request**.
* **Problema:** El disparador de chat no lograba pasar los datos del usuario al nodo de petición HTTP de manera efectiva. El flujo se mantenía en estado "cargando" indefinidamente, indicando una ruptura en la cadena de paso de parámetros.

### E. Alternativa mediante Webhooks y Chat Público

* **Acción:** Se intentó exponer el chat mediante una URL pública y usar un **Webhook** para capturar y procesar los datos.
* **Resultado:** Se replicó el mismo síntoma de carga infinita al intentar unir el Webhook con la lógica de respuesta del chat. En ejecuciones separadas, los datos no llegaban al nodo de destino, invalidando la interactividad necesaria para un agente.
![n8n_chat_webhook](/Documentacion/IMG/n8n_chat_webhook.jpg)

## 3. Análisis de Causas Raíz

1. **Incompatibilidad de Flujo de Datos:** Se identificó un fallo en la arquitectura interna de n8n donde el **Chat Trigger** no lograba inyectar el input del usuario en nodos manuales (HTTP), bloqueando la ejecución.
2. **Ruptura de la Respuesta (Response Loop):** La imposibilidad de cerrar el ciclo "Petición-Respuesta" entre el disparador y el servidor externo (Ollama) causó que la interfaz de usuario se quedara en espera perpetua, independientemente del rendimiento del modelo de IA.

## 4. Conclusión

Pese a que el servidor de IA (Ollama) es totalmente funcional y responde correctamente a peticiones externas, **n8n no ha demostrado ser capaz de gestionar el flujo de datos necesario** para conectar sus disparadores de interfaz con la lógica manual de la API. Dada la persistencia de los estados de "carga infinita" y la nula transferencia de datos entre nodos de entrada y salida, se desiste de esta plataforma para el desarrollo del agente.
