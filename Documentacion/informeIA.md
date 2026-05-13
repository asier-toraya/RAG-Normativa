# Sistema multi-agente de auditoría jurídica con IA

## 1. Introducción

El presente proyecto tiene como objetivo el diseño e implementación de un sistema inteligente basado en múltiples modelos de inteligencia artificial especializados, orientado al análisis, interpretación y auditoría de información jurídica.

El sistema se basa en una arquitectura multi-agente, donde cada agente desempeña una función específica dentro del proceso de razonamiento jurídico, permitiendo una mayor precisión, escalabilidad y trazabilidad en la generación de respuestas.



# 2. Objetivo del sistema

El objetivo principal es desarrollar una arquitectura capaz de:

- Analizar información jurídica compleja.
- Clasificar normativa por ramas del derecho.
- Integrar jurisprudencia relevante.
- Detectar conflictos normativos.
- Generar informes estructurados y coherentes.
- Automatizar el proceso de auditoría legal mediante IA.


# 3. Arquitectura general del sistema

El sistema se ha diseñado siguiendo una arquitectura jerárquica, pensada para simular un entorno de análisis colaborativo entre distintos “especialistas” de inteligencia artificial. En el centro de esta estructura se encuentra un orquestador central, que actúa como cerebro coordinador, y a su alrededor varios subagentes especializados que se encargan de analizar cada parte del problema desde un enfoque concreto.

Esta organización permite que el sistema no dependa de un único modelo que lo haga todo, sino que distribuya la carga de trabajo de forma inteligente, mejorando la precisión, la trazabilidad de los resultados y la calidad del análisis final.



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

## 3.2.1 Determinación de la competencia procesal y de los órganos judiciales competentes

Además de identificar la normativa material aplicable, el subagente normativo incorpora un análisis de derecho procesal orientado a identificar el órgano judicial competente para conocer de cada asunto. Para ello, no se limita a determinar la rama material del derecho implicada, sino también vincula cada supuesto con la estructura orgánica del Poder Judicial, teniendo en cuenta la distribución de competencias entre jueces, tribunales y secciones especializadas.

Este agente analiza la competencia desde una triple perspectiva, objetiva, para determinar qué órgano debe conocer del asunto según la materia o la gravedad del hecho; funcional, para distinguir qué órgano interviene en fase de instrucción, enjuiciamiento, recurso o ejecución; y territorial, para concretar la circunscripción judicial competente en función del lugar de comisión del hecho o del ámbito jurisdiccional correspondiente. De este modo, el sistema puede reconstruir no solo qué norma resulta aplicable, sino también cuál es el itinerario procesal adecuado dentro de la organización judicial. 

A partir de esta lógica, el subagente puede identificar la intervención de los distintos órganos judiciales reconocidos en la estructura vigente, entre ellos los jueces y juezas de paz, los Tribunales de Instancia, las Audiencias Provinciales, los Tribunales Superiores de Justicia, el Tribunal Central de Instancia, la Audiencia Nacional y el Tribunal Supremo. Asimismo, puede distinguir cuándo un asunto corresponde a secciones ordinarias de instrucción o de lo penal y cuándo debe atribuirse a órganos especializados, como las secciones contencioso-administrativo.

En el ámbito penal, esta capacidad resulta especialmente relevante, ya que permite relacionar la competencia con criterios procesales concretos, como la pena prevista, la condición de aforado de la persona investigada, la existencia de competencias centralizadas de ámbito nacional o la presencia de materias especialmente atribuidas a órganos específicos. Así, el sistema puede diferencias, por ejemplo, entre asuntos cuya instrucción corresponde a secciones de instrucción de los Tribunales de Instancia, causas atribuidas al Tribunal Central de Instancia, procedimientos competencia de las Audiencias Provinciales o supuestos reservados al Tribunal Supremo o a los Tribunales Superiores de justicia. 

Además, el subagente puede incorporar reglas especiales de atribución competencial derivadas de la normativa procesal, como las relativas a delitos leves, aforamientos, recursos, decomiso autónomo o reconocimiento mutuo de resoluciones penales en la Unión Europea. Esta funcionalidad refuerza la precisión del sistema, porque no solo permite saber qué derecho sustantivo rige el caso, sino también ante qué órgano debe articularse la actuación judicial y qué recorrido procesal puede seguir posteriormente. 

### Reglas de asignación

1. Regla general penal

Si el supuesto constituye un posible delito común no atribuido a órgano especial, la instrucción corresponde a la Sección de Instrucción del Tribunal de Instancia del lugar de comisión del hecho, y el enjuiciamiento dependerá de la pena prevista: si la pena de prisión supera los 5 años, o la pena de otra naturaleza no supera los 10 años, conocerá la Sección de lo Penal del Tribunal de Instancia; en los demás casos, será competente la Audiencia Provincial.

Este supuesto sirve para la mayoría de incidentes empresariales con dimensión penal ordinaria: acceso ilícito a sistemas, daños informáticos, descubrimiento y revelación de secretos, estafas informáticas, sabotaje interno, borrado de evidencias o exfiltración de datos siempre y cuando no entren en competencia centralizada.

2. Competencia centralizada

Si el caso se encuentra en el ámbito de la Audiencia Nacional , la instrucción corresponde a la Sección de Instrucción del Tribunal Central de Instancia y el enjuiciamiento se reparte según gravedad entre la Sección de lo Penal del Tribunal Central de Instancia y la Sala de lo Penal de la Audiencia Nacional.

Esta vía centralizada aplica especialmente cuando el hecho afecte a delitos atribuidos a la Audiencia Nacional, tales como terrorismo, delitos cometidos fuera del territorio nacional cuando deban ser enjuiciados en España, determinados supuestos vinculados a criminalidad organizada de especial alcance, delitos atribuidos a la Fiscalía Europea, o procedimientos de extracción y cooperación penal europea.

### Órgano según tipo de incidente

3. Incidentes de empresa “ordinarios”
Para un ransomware contra una pyme, una intrusión con robo de credenciales, un empleado que extrae bases de datos, un fraude BEC, una alteración de registros, o la destrucción de evidencias digitales, el criterio por defecto será la Sección de Instrucción del Tribunal de Instancia para investigar; después, Sección de lo Penal del Tribunal de Instancia si la pena encaja en el tramo de hasta 5 años de prisión o hasta 10 años en otras penas, y Audiencia Provincial si supera ese umbral. 

Operativamente, el subagente puede etiquetar esto asuntos como “penal ordinario empresarial” salvo que detecte un elemento desplazador de competencia, como aforamiento, terrorismo, dimensión supraprovincial especialmente centralizada, hechos en el extranjero o atribución a la Fiscalía Europea.

4. Ciberincidentes

Si el incidente tecnológico incluye acoso digital, difusión íntima, sextorsión, amenazas, hostigamiento, control mediante spyware o vigilancia digital dentro de un contexto de violencia sobre la mujer, la competencia instructora corresponde a la Sección de Violencia sobre la Mujer; además, esta sección puede adoptar órdenes de protección y conocer también de delitos leves atribuidos por ley en ese ámbito.

Si los hechos recaen sobre niños, niñas o adolescentes, como grooming, explotación, difusión de material íntimo, amenazas, control tecnológico o delitos violentos con componente digital contra menores, la instrucción corresponde a la Sección de Violencia sobre la Infancia y la Adolescencia, salvo que concurra también violencia sobre la mujer.

5. Ejecución penitenciaria

Si el asunto ya no consiste en investigar o enjuiciar el ciberincidente, sino en controlar el cumplimiento de pena, sanciones penitenciarias o derechos del penado condenado por delitos informáticos, la competencia es de la Sección de Vigilancia Penitenciaria del Tribunal de Instancia, o de la Sección de Vigilancia Penitenciaria del Tribunal Central de Instancia cuando la condena derive de delitos competencia de la Audiencia Nacional.

### Casos administrativos regulatorios

6. Actos de autoridades estatales
   
Si el conflicto gira en torno a actos, disposiciones o decisiones de autoridades, organismos u órganos con competencia en todo el territorio nacional, la vía ya no es penal ordinaria, sino contencioso-administrativa centralizada, y conocerá la Sección de lo Contencioso-Administrativo del Tribunal Central de Instancia en primera o única instancia.
También se atribuyen a esa sección autorizaciones especialmente relevantes para el ámbito digital, como la cesión de datos por prestadores de servicios de la sociedad de la información, medidas de interrupción o retirada de contenidos, limitaciones de acceso previstas en la normativa europea de servicios digitales, y requerimientos de información impulsados por la Agencia Española de Protección de Datos u otras autoridades administrativas independientes estatales.

7. Casos administrativos no centralizados

Si el conflicto administrativo tecnológico afecta a actuaciones de administraciones no estatales de ámbito general nacional, la competencia deberá reconducirse a la Sección de lo Contencioso-Administrativo del Tribunal de Instancia cuando proceda según territorio y materia.


## 3.3 Subagente de jurisprudencia

El subagente de jurisprudencia se encarga de aportar la visión práctica del derecho a través del análisis de decisiones judiciales. Su objetivo es complementar la normativa con cómo realmente se interpreta y aplica en los tribunales.

Entre sus funciones principales está el análisis de sentencias relevantes, seleccionando aquellas resoluciones que guardan relación con el caso y que pueden aportar criterios útiles para su resolución.

También identifica precedentes judiciales, es decir, casos anteriores similares que ayudan a orientar la interpretación del problema actual y a prever posibles líneas de decisión.

Además, relaciona la jurisprudencia con la normativa aplicable, estableciendo cómo los tribunales han interpretado determinados artículos o disposiciones legales en situaciones concretas.

Por último, detecta posibles interpretaciones divergentes entre tribunales, señalando cuando existen distintos criterios sobre una misma norma, lo que permite tener una visión más completa y realista del marco jurídico.


## 3.4 Subagente de actualización normativa

El subagente de actualización normativa se encarga de mantener el sistema al día con los cambios legales que se producen de forma continua. Su función es asegurar que el análisis jurídico siempre se base en normativa vigente y no desactualizada.

Para ello, realiza la revisión de cambios legislativos, detectando modificaciones, derogaciones o nuevas disposiciones publicadas en fuentes oficiales.

También se ocupa de la integración de nuevas normativas, incorporando al sistema cualquier ley, reglamento o actualización relevante que pueda afectar al análisis de los casos.

Por último, realiza la comparación entre versiones legales, identificando qué ha cambiado entre una normativa antigua y su versión actualizada, lo que permite entender el impacto real de las modificaciones en su aplicación.

## 3.5 Sistema de herramientas (MCP / Skills)

El sistema se apoya en un conjunto de herramientas externas que amplían las capacidades del modelo de lenguaje y permiten ejecutar acciones reales más allá del razonamiento. Estas herramientas se integran mediante un enfoque modular basado en MCP (Model Context Protocol) y “skills”, lo que permite añadir o sustituir componentes sin modificar la arquitectura principal.

### Automatización web (Playwright)

Playwright es una herramienta de automatización de navegadores que permite controlar páginas web de forma programática. En este sistema se utiliza para tareas como scraping, navegación automatizada, extracción de información y ejecución de flujos en sitios dinámicos.

Su principal ventaja es que puede interactuar con páginas como lo haría un usuario real (clics, formularios, navegación), lo que la hace especialmente útil en entornos donde las APIs no están disponibles o son limitadas. Además, combinada con MCP, permite que los agentes de IA ejecuten acciones en la web de forma estructurada y controlada.

### Orquestación de flujos (n8n)

n8n es una plataforma de automatización de workflows utilizada para:

- Automatizar procesos repetitivos.
- Conectar APIs y bases de datos.
- Gestionar flujos de información entre módulos.

Su enfoque visual y modular facilita construir pipelines complejos donde cada paso puede ser controlado, monitorizado y adaptado según el resultado anterior.

### Ejecución de modelos locales (vLLM / LM Studio)

vLLM es un motor optimizado para servir modelos de lenguaje de forma eficiente, especialmente en entornos de alta carga. Permite ejecutar inferencias rápidas y escalables, reduciendo latencia y coste computacional.

Por otro lado, LM Studio es una herramienta que facilita la ejecución de modelos locales de IA en entornos de usuario, permitiendo trabajar con modelos sin depender completamente de servicios en la nube.

Ambas soluciones se integran en el sistema para:

- Ejecutar modelos localmente.
- Reducir dependencia de servicios externos.
- Mejorar privacidad.
- Optimizar rendimiento.

### Enfoque general del sistema

La combinación de MCP + skills permite que cada herramienta funcione como un “módulo especializado”. Esto hace que el sistema sea:

- Extensible.
- Flexible.
- Escalable.

En conjunto, este enfoque convierte el sistema en una arquitectura híbrida entre inteligencia artificial y automatización real, donde los modelos no solo “piensan”, sino que también ejecutan acciones concretas en el entorno digital.

## 3.6 Agente de formateo de respuesta

El agente de formateo de respuesta es el módulo encargado de dar forma final a toda la información generada por el sistema. No participa en el análisis ni en la toma de decisiones, sino que su función principal es transformar los resultados de los distintos agentes en una salida clara, coherente y bien presentada.

Su trabajo consiste en recoger la información generada por el resto de módulos y unificarla en un único texto, evitando que aparezca desordenada o con estilos diferentes. De esta manera, consigue que todo el contenido tenga continuidad y sea fácil de seguir.

También adapta las respuestas al formato de informe, asegurando una redacción homogénea y una estructura lógica que facilite la lectura. Esto permite que el resultado final no solo sea correcto a nivel de contenido, sino también comprensible y directamente utilizable.

En conjunto, este agente actúa como la capa final del sistema, encargada de convertir todo el procesamiento interno en una respuesta limpia, organizada y lista para su entrega.


# 4. Flujo de funcionamiento

El sistema sigue un flujo de trabajo secuencial y modular que permite transformar una consulta jurídica en un informe final estructurado. Cada fase tiene una función concreta dentro del proceso global.

## 4.1 Recepción de la consulta

El proceso comienza cuando el orquestador central recibe la consulta jurídica. En este punto se captura la información inicial del caso y se prepara para su análisis.

## 4.2 Clasificación inicial

El orquestador realiza una primera interpretación del problema, identificando su naturaleza, el área del derecho implicada y el nivel de complejidad. Esto permite definir cómo se abordará el análisis.

## 4.3 Distribución de tareas

Una vez clasificado el caso, el sistema reparte el trabajo entre los distintos subagentes especializados, asignando a cada uno una parte concreta del análisis según su función.

## 4.4 Procesamiento paralelo

Los subagentes trabajan de forma simultánea, analizando la información desde diferentes perspectivas (normativa, jurisprudencial, actualización, etc.), lo que optimiza el tiempo de respuesta.

## 4.5 Integración de resultados

El orquestador recoge los resultados generados por cada subagente y los combina en una única visión global del caso, asegurando coherencia entre todas las partes.

## 4.6 Resolución de conflictos

Si aparecen contradicciones entre fuentes normativas o interpretaciones jurisprudenciales, el sistema las detecta y las compara para determinar la opción más consistente o relevante.

## 4.7 Generación del informe final

Finalmente, toda la información se organiza y se presenta en un informe estructurado, claro y coherente, listo para su uso.


# 5. Tecnologías utilizadas

El sistema se construye sobre una combinación de tecnologías que permiten tanto el razonamiento avanzado como la ejecución de acciones automatizadas. Esta mezcla hace posible crear una arquitectura híbrida donde la inteligencia artificial no solo analiza información, sino que también interactúa con sistemas externos.

## Modelos de lenguaje (LLMs locales o API)

Son el núcleo de la capacidad de razonamiento del sistema. Estos modelos se utilizan para interpretar consultas, generar análisis y coordinar la lógica entre agentes. Pueden ejecutarse tanto mediante APIs en la nube como en entornos locales, dependiendo de las necesidades de rendimiento, privacidad o control.

## Frameworks de automatización (n8n)

n8n se utiliza como herramienta de orquestación de procesos. Permite conectar servicios, APIs y acciones automatizadas sin necesidad de programar cada integración desde cero. Esto facilita la creación de flujos de trabajo complejos entre los distintos módulos del sistema.

## Herramientas de scraping y navegación (Playwright)

Playwright permite automatizar la interacción con páginas web. Se emplea para extraer información dinámica, navegar por sitios y simular el comportamiento de un usuario real. Es especialmente útil cuando no existen APIs disponibles o se requiere acceder a contenido actualizado en tiempo real.

## Sistemas locales de IA (vLLM y LM Studio)

Estas herramientas permiten ejecutar modelos de lenguaje de forma local, optimizando el rendimiento y reduciendo la dependencia de servicios externos. vLLM está orientado a eficiencia y escalabilidad, mientras que LM Studio facilita un entorno más accesible para la ejecución y prueba de modelos.

## Arquitecturas multi-agente

El sistema está basado en una arquitectura multi-agente, donde diferentes modelos o módulos especializados trabajan de forma coordinada. Cada agente tiene una función concreta, lo que permite dividir el problema en partes más pequeñas y mejorar la precisión del análisis final.

# 6. Metodología

El desarrollo del sistema se basa en una arquitectura modular y escalable, diseñada para que cada parte funcione de manera independiente pero coordinada dentro del conjunto. Esto permite construir el sistema por bloques, facilitando su evolución y adaptación.

Cada agente se desarrolla, prueba y optimiza de forma separada, lo que evita dependencias innecesarias entre módulos y permite mejorar componentes concretos sin afectar al resto del sistema.

Se aplica un enfoque claro de separación de responsabilidades, donde cada módulo tiene una función específica bien definida dentro de la arquitectura. Gracias a esto, el sistema gana en organización y claridad estructural.

Este enfoque aporta varias ventajas clave: una mayor facilidad de mantenimiento, ya que los cambios se pueden realizar de forma aislada; una mejor escalabilidad, al poder añadir nuevos agentes o herramientas sin reestructurar el sistema completo; y la reutilización de componentes, permitiendo integrar módulos ya desarrollados en otros contextos o proyectos.


# 7. Resultados esperados

Con la implementación de este sistema se espera obtener una herramienta capaz de realizar un análisis jurídico más completo, preciso y estructurado que el de un modelo único tradicional.

El sistema debería ser capaz de analizar casos jurídicos complejos, descomponiéndolos en partes más manejables y abordándolos desde distintas perspectivas especializadas.

También se espera que pueda integrar múltiples fuentes de información, combinando normativa, jurisprudencia y datos actualizados para ofrecer una visión global del caso.

Otro resultado clave es la generación de informes estructurados y fiables, con una organización clara que facilite su lectura y comprensión, manteniendo coherencia entre todas las partes del análisis.

Por último, el sistema debe reducir errores mediante verificación cruzada entre agentes, comparando resultados y detectando posibles inconsistencias antes de generar la respuesta final.

# 8. Conclusión

Este proyecto plantea un enfoque basado en inteligencia artificial distribuida aplicada al ámbito jurídico, utilizando una arquitectura multi-agente para dividir y especializar el análisis de la información.

Gracias a esta estructura, el sistema no depende de un único modelo, sino de varios componentes que colaboran entre sí para interpretar, contrastar y organizar la información legal de forma más completa.

Esto permite mejorar la eficiencia en el procesamiento de casos, aumentar la precisión en el análisis y aportar mayor trazabilidad en las decisiones generadas por el sistema.

En conjunto, la propuesta supone una evolución frente a los sistemas tradicionales basados en un solo modelo de IA, al introducir una forma más modular, escalable y especializada de trabajar con información jurídica.