# Sistema multi-agente de auditoría jurídica con IA

## 1. Introducción

El presente proyecto tiene como objetivo el diseño e implementación de un sistema inteligente basado en múltiples modelos de inteligencia artificial especializados, orientado al análisis, interpretación y auditoría de información jurídica.

El sistema se basa en una arquitectura multi-agente, donde cada agente desempeña una función específica dentro del proceso de razonamiento jurídico, permitiendo una mayor precisión, escalabilidad y trazabilidad en la generación de respuestas.

---

# 2. Objetivo del sistema

El objetivo principal es desarrollar una arquitectura capaz de:

- Analizar información jurídica compleja.
- Clasificar normativa por ramas del derecho.
- Integrar jurisprudencia relevante.
- Detectar conflictos normativos.
- Generar informes estructurados y coherentes.
- Automatizar el proceso de auditoría legal mediante IA.

---

# 3. Arquitectura general del sistema

El sistema se ha diseñado siguiendo una arquitectura jerárquica, pensada para simular un entorno de análisis colaborativo entre distintos “especialistas” de inteligencia artificial. En el centro de esta estructura se encuentra un orquestador central, que actúa como cerebro coordinador, y a su alrededor varios subagentes especializados que se encargan de analizar cada parte del problema desde un enfoque concreto.

Esta organización permite que el sistema no dependa de un único modelo que lo haga todo, sino que distribuya la carga de trabajo de forma inteligente, mejorando la precisión, la trazabilidad de los resultados y la calidad del análisis final.

---

## 3.1 Orquestador central

El orquestador central es el componente principal del sistema. Se puede entender como el “director de orquesta” que no ejecuta directamente el análisis profundo, pero sí decide cómo, cuándo y quién debe hacerlo.

Su función principal es recibir una consulta o caso jurídico en bruto, interpretarlo y transformarlo en un conjunto de tareas más pequeñas y manejables. A partir de ahí, decide qué subagente es el más adecuado para cada parte del análisis, asegurando que cada uno trabaje sobre su área de especialización.

Por ejemplo, si llega un caso complejo, el orquestador puede identificar que una parte requiere análisis normativo, otra análisis de precedentes legales y otra verificación de coherencia o riesgos. En lugar de abordar todo de forma lineal, divide el problema y lo distribuye de forma estratégica.

Además, el orquestador no solo reparte tareas, sino que también supervisa el proceso completo. Esto implica:

- Controlar el flujo de información entre agentes para evitar pérdidas o contradicciones.
- Coordinar los resultados parciales para que tengan coherencia entre sí.
- Resolver posibles conflictos entre conclusiones diferentes aportadas por los subagentes.
- Mantener una visión global del caso en todo momento.

Una vez que los subagentes han finalizado su trabajo, el orquestador recoge todos los resultados, los analiza en conjunto y realiza un proceso de síntesis. En esta fase final, elimina redundancias, resuelve inconsistencias y estructura la información de manera clara y comprensible.

El resultado es una respuesta final unificada, coherente y bien organizada, que no es simplemente una suma de partes, sino una interpretación global del caso basada en múltiples perspectivas especializadas.

En resumen, el orquestador central actúa como el elemento de control, coordinación y síntesis del sistema, permitiendo que la inteligencia colectiva de los subagentes se convierta en un único análisis sólido y estructurado.

---

## 3.2 Subagente normativo

El subagente normativo es uno de los componentes clave dentro de la arquitectura del sistema, ya que se encarga de interpretar, clasificar y estructurar toda la información relacionada con el marco legal aplicable a cada caso. Su objetivo principal es transformar el contenido jurídico en conocimiento organizado y utilizable por el resto del sistema, evitando ambigüedades y facilitando un análisis más preciso.

Este agente trabaja como un “analista de leyes”, capaz de identificar qué normas son relevantes en cada situación y cómo deben aplicarse en función del contexto del caso.

En primer lugar, el subagente normativo realiza una clasificación de la normativa jurídica, diferenciando entre dos grandes niveles:

### Normas primarias

Son aquellas disposiciones jurídicas que establecen derechos, obligaciones y prohibiciones de forma directa. Incluyen leyes, reglamentos y disposiciones con fuerza normativa que afectan de manera inmediata a los sujetos implicados. Este tipo de normas constituye la base principal sobre la que se fundamenta cualquier análisis jurídico.

### Normas secundarias

Son normas que no regulan directamente conductas, sino que organizan, interpretan o complementan a las normas primarias. Incluyen criterios de aplicación, procedimientos, mecanismos de control y disposiciones interpretativas. Su función es garantizar que las normas primarias se apliquen de forma correcta y coherente dentro del sistema jurídico.

Además de esta clasificación general, el subagente normativo también organiza la información según la rama del derecho a la que pertenece el caso, lo que permite una segmentación más precisa del análisis.

### Derecho Civil

Se encarga de todo lo relacionado con las relaciones jurídicas entre particulares, como contratos, obligaciones, propiedad, familia o herencias. El agente identifica normas aplicables a conflictos privados y establece qué disposiciones regulan cada situación concreta.

### Derecho Penal

Analiza conductas que pueden ser constitutivas de delito, identificando los artículos del código penal aplicables, así como las consecuencias jurídicas asociadas. También permite distinguir entre distintos tipos de infracciones y su gravedad.

### Derecho Administrativo

Se centra en la relación entre los ciudadanos y la administración pública. Aquí el subagente identifica normativas relacionadas con sanciones administrativas, procedimientos administrativos, licencias, recursos y funcionamiento de las instituciones públicas.

Otro aspecto fundamental del subagente normativo es su capacidad para distinguir entre diferentes jurisdicciones, ya que la aplicación de la ley puede variar significativamente según el ámbito territorial o institucional.

### España

El agente analiza la normativa nacional, incluyendo la Constitución, leyes orgánicas, leyes ordinarias y reglamentos estatales, así como su interpretación dentro del sistema jurídico español.

### Unión Europea

También es capaz de identificar normativa comunitaria, como reglamentos, directivas y decisiones del Tribunal de Justicia de la Unión Europea, evaluando su aplicabilidad directa o su necesidad de transposición al ordenamiento nacional.

En conjunto, este subagente no solo clasifica información legal, sino que la estructura de forma lógica y jerárquica, permitiendo que el sistema pueda comprender con precisión qué normativa es relevante, cómo se relaciona entre sí y en qué contexto debe aplicarse. Esto resulta fundamental para garantizar que el análisis jurídico final sea coherente, fundamentado y ajustado a la realidad normativa vigente.

---

## 3.2.1 Determinación de la competencia procesal y de los órganos judiciales competentes

Además de identificar la normativa material aplicable, el subagente normativo incorpora un análisis de derecho procesal orientado a identificar el órgano judicial competente para conocer de cada asunto. Para ello, no se limita a determinar la rama material del derecho implicada, sino también vincula cada supuesto con la estructura orgánica del Poder Judicial, teniendo en cuenta la distribución de competencias entre jueces, tribunales y secciones especializadas.

Este agente analiza la competencia desde una triple perspectiva:

- Objetiva, para determinar qué órgano debe conocer del asunto según la materia o la gravedad del hecho.
- Funcional, para distinguir qué órgano interviene en fase de instrucción, enjuiciamiento, recurso o ejecución.
- Territorial, para concretar la circunscripción judicial competente en función del lugar de comisión del hecho o del ámbito jurisdiccional correspondiente.

De este modo, el sistema puede reconstruir no solo qué norma resulta aplicable, sino también cuál es el itinerario procesal adecuado dentro de la organización judicial.

A partir de esta lógica, el subagente puede identificar la intervención de los distintos órganos judiciales reconocidos en la estructura vigente, entre ellos:

- Jueces y juezas de paz.
- Tribunales de Instancia.
- Audiencias Provinciales.
- Tribunales Superiores de Justicia.
- Tribunal Central de Instancia.
- Audiencia Nacional.
- Tribunal Supremo.

Asimismo, puede distinguir cuándo un asunto corresponde a secciones ordinarias de instrucción o de lo penal y cuándo debe atribuirse a órganos especializados, como las secciones contencioso-administrativas.

En el ámbito penal, esta capacidad resulta especialmente relevante, ya que permite relacionar la competencia con criterios procesales concretos, como:

- La pena prevista.
- La condición de aforado.
- La existencia de competencias centralizadas.
- La presencia de materias atribuidas a órganos específicos.

Así, el sistema puede diferenciar, por ejemplo, entre asuntos cuya instrucción corresponde a secciones de instrucción de los Tribunales de Instancia, causas atribuidas al Tribunal Central de Instancia, procedimientos competencia de las Audiencias Provinciales o supuestos reservados al Tribunal Supremo o a los Tribunales Superiores de Justicia.

Además, el subagente puede incorporar reglas especiales de atribución competencial derivadas de la normativa procesal, como las relativas a:

- Delitos leves.
- Aforamientos.
- Recursos.
- Decomiso autónomo.
- Reconocimiento mutuo de resoluciones penales en la Unión Europea.

Esta funcionalidad refuerza la precisión del sistema, porque no solo permite saber qué derecho sustantivo rige el caso, sino también ante qué órgano debe articularse la actuación judicial y qué recorrido procesal puede seguir posteriormente.

### Reglas de asignación

#### Regla general penal

Si el supuesto constituye un posible delito común no atribuido a órgano especial, la instrucción corresponde a la Sección de Instrucción del Tribunal de Instancia del lugar de comisión del hecho, y el enjuiciamiento dependerá de la pena prevista.

Si la pena de prisión supera los 5 años, o la pena de otra naturaleza supera los 10 años, conocerá la Audiencia Provincial. En los demás casos será competente la Sección de lo Penal del Tribunal de Instancia.

Este supuesto sirve para la mayoría de incidentes empresariales con dimensión penal ordinaria:

- Acceso ilícito a sistemas.
- Daños informáticos.
- Descubrimiento y revelación de secretos.
- Estafas informáticas.
- Sabotaje interno.
- Borrado de evidencias.
- Exfiltración de datos.

Siempre y cuando no entren en competencia centralizada.

#### Competencia centralizada

Si el caso se encuentra en el ámbito de la Audiencia Nacional, la instrucción corresponde a la Sección de Instrucción del Tribunal Central de Instancia y el enjuiciamiento se reparte según gravedad entre la Sección de lo Penal del Tribunal Central de Instancia y la Sala de lo Penal de la Audiencia Nacional.

Esta vía centralizada aplica especialmente cuando el hecho afecte a delitos atribuidos a la Audiencia Nacional, tales como:

- Terrorismo.
- Delitos cometidos fuera del territorio nacional.
- Criminalidad organizada de especial alcance.
- Delitos atribuidos a la Fiscalía Europea.
- Procedimientos de extradición y cooperación penal europea.

### Órgano según tipo de incidente

#### Incidentes de empresa “ordinarios”

Para un ransomware contra una pyme, una intrusión con robo de credenciales, un empleado que extrae bases de datos, un fraude BEC, una alteración de registros o la destrucción de evidencias digitales, el criterio por defecto será:

- Sección de Instrucción del Tribunal de Instancia para investigar.
- Sección de lo Penal del Tribunal de Instancia si la pena encaja en el tramo correspondiente.
- Audiencia Provincial si supera dicho umbral.

Operativamente, el subagente puede etiquetar estos asuntos como “penal ordinario empresarial”, salvo que detecte un elemento desplazador de competencia.

#### Ciberincidentes

Si el incidente tecnológico incluye:

- Acoso digital.
- Difusión íntima.
- Sextorsión.
- Amenazas.
- Hostigamiento.
- Spyware.
- Vigilancia digital.

Dentro de un contexto de violencia sobre la mujer, la competencia instructora corresponde a la Sección de Violencia sobre la Mujer.

Si los hechos recaen sobre menores, como:

- Grooming.
- Explotación.
- Difusión de material íntimo.
- Amenazas.
- Control tecnológico.

La instrucción corresponde a la Sección de Violencia sobre la Infancia y la Adolescencia.

#### Ejecución penitenciaria

Si el asunto consiste en controlar el cumplimiento de penas o derechos penitenciarios derivados de delitos informáticos, la competencia será de:

- La Sección de Vigilancia Penitenciaria del Tribunal de Instancia.
- O la Sección de Vigilancia Penitenciaria del Tribunal Central de Instancia si deriva de delitos competencia de la Audiencia Nacional.

### Casos administrativos regulatorios

#### Actos de autoridades estatales

Si el conflicto gira en torno a actos, disposiciones o decisiones de autoridades con competencia nacional, conocerá la Sección de lo Contencioso-Administrativo del Tribunal Central de Instancia.

También se atribuyen a esta sección:

- Cesión de datos.
- Retirada de contenidos.
- Limitaciones de acceso.
- Requerimientos impulsados por la Agencia Española de Protección de Datos.

#### Casos administrativos no centralizados

Si el conflicto administrativo tecnológico afecta a actuaciones de administraciones no estatales, la competencia corresponderá a la Sección de lo Contencioso-Administrativo del Tribunal de Instancia.

---

## 3.3 Subagente de jurisprudencia

El subagente de jurisprudencia se encarga de aportar la visión práctica del derecho a través del análisis de decisiones judiciales.

Entre sus funciones principales está:

- El análisis de sentencias relevantes.
- La identificación de precedentes judiciales.
- La relación entre jurisprudencia y normativa.
- La detección de interpretaciones divergentes.

Además, relaciona la jurisprudencia con la normativa aplicable, estableciendo cómo los tribunales han interpretado determinados artículos o disposiciones legales en situaciones concretas.

---

## 3.4 Subagente de actualización normativa

El subagente de actualización normativa se encarga de mantener el sistema actualizado con los cambios legislativos.

### Funciones

- Revisión de cambios legislativos.
- Detección de derogaciones y modificaciones.
- Integración de nuevas normativas.
- Comparación entre versiones legales.

Esto permite asegurar que el análisis jurídico siempre se base en normativa vigente y actualizada.

---

## 3.5 Sistema de herramientas (MCP / Skills)

El sistema se apoya en herramientas externas que amplían las capacidades del modelo de lenguaje y permiten ejecutar acciones reales más allá del razonamiento.

### Automatización web (Playwright)

Playwright es una herramienta de automatización de navegadores que permite controlar páginas web de forma programática.

Se utiliza para:

- Scraping.
- Navegación automatizada.
- Extracción de información.
- Automatización de procesos web.

### Orquestación de flujos (n8n)

n8n es una plataforma de automatización de workflows utilizada para:

- Automatizar procesos repetitivos.
- Conectar APIs y bases de datos.
- Gestionar flujos de información entre módulos.

### Ejecución de modelos locales (vLLM / LM Studio)

Estas herramientas permiten:

- Ejecutar modelos localmente.
- Reducir dependencia de servicios externos.
- Mejorar privacidad.
- Optimizar rendimiento.

### Enfoque general del sistema

La combinación de MCP y skills permite una arquitectura:

- Extensible.
- Flexible.
- Escalable.

En conjunto, convierte el sistema en una arquitectura híbrida entre inteligencia artificial y automatización real.

---

## 3.6 Agente de formateo de respuesta

El agente de formateo de respuesta es el módulo encargado de dar forma final a toda la información generada por el sistema.

### Funciones

- Unificar información.
- Mantener coherencia textual.
- Adaptar el contenido a formato informe.
- Facilitar la lectura y comprensión.

Actúa como la capa final del sistema, convirtiendo el procesamiento interno en una respuesta organizada y lista para su entrega.

---

# 4. Flujo de funcionamiento

## 4.1 Recepción de la consulta

El proceso comienza cuando el orquestador central recibe la consulta jurídica.

## 4.2 Clasificación inicial

El sistema identifica:

- Naturaleza del problema.
- Rama del derecho implicada.
- Nivel de complejidad.

## 4.3 Distribución de tareas

El trabajo se reparte entre los subagentes especializados.

## 4.4 Procesamiento paralelo

Los subagentes trabajan simultáneamente.

## 4.5 Integración de resultados

El orquestador combina todos los resultados obtenidos.

## 4.6 Resolución de conflictos

Se detectan contradicciones normativas o jurisprudenciales.

## 4.7 Generación del informe final

El sistema genera un informe estructurado, coherente y comprensible.

---

# 5. Tecnologías utilizadas

## Modelos de lenguaje (LLMs locales o API)

Se utilizan para:

- Interpretación jurídica.
- Generación de análisis.
- Coordinación entre agentes.

## Frameworks de automatización (n8n)

Permiten integrar procesos y servicios externos.

## Herramientas de scraping y navegación (Playwright)

Utilizadas para extracción de información y automatización web.

## Sistemas locales de IA (vLLM y LM Studio)

Permiten ejecutar modelos de lenguaje localmente.

## Arquitecturas multi-agente

Facilitan:

- Especialización.
- Modularidad.
- Escalabilidad.

---

# 6. Metodología

El desarrollo del sistema se basa en una arquitectura modular y escalable.

### Características

- Desarrollo independiente de agentes.
- Separación clara de responsabilidades.
- Escalabilidad.
- Reutilización de componentes.
- Facilidad de mantenimiento.

---

# 7. Resultados esperados

Con la implementación de este sistema se espera:

- Analizar casos jurídicos complejos.
- Integrar múltiples fuentes legales.
- Generar informes fiables y estructurados.
- Reducir errores mediante verificación cruzada.
- Mejorar precisión y trazabilidad.

---

# 8. Conclusión

Este proyecto plantea un enfoque basado en inteligencia artificial distribuida aplicada al ámbito jurídico, utilizando una arquitectura multi-agente para dividir y especializar el análisis de la información.

Gracias a esta estructura, el sistema no depende de un único modelo, sino de varios componentes que colaboran entre sí para interpretar, contrastar y organizar la información legal de forma más completa.

Esto permite mejorar la eficiencia en el procesamiento de casos, aumentar la precisión en el análisis y aportar mayor trazabilidad en las decisiones generadas por el sistema.

En conjunto, la propuesta supone una evolución frente a los sistemas tradicionales basados en un solo modelo de IA, al introducir una forma más modular, escalable y especializada de trabajar con información jurídica.