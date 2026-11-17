---
name: AI-Humanizer
description: Redacta o reescribe un texto sin los rasgos típicos de la escritura generada por IA. Úsala cuando el usuario diga "Crea documento humanizado" (o una variante evidente), tanto para escribir un documento nuevo como para reescribir uno existente.
---

# AI-Humanizer

Basada en la guía de Wikipedia "Signs of AI writing" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), que cataloga los patrones que delatan texto de IA. Esta habilidad los usa al revés: como lista de qué evitar.

## Principio rector

Los rasgos son síntomas de problemas de fondo: afirmaciones sin sustento, relleno, tono promocional y falta de datos concretos. Quitar palabras sueltas no basta. Un texto humano es **específico**: nombres, cifras, fechas, ejemplos y fuentes verificables.

Reglas de honestidad:
- Nunca inventes datos, citas, cifras, enlaces, DOI ni fuentes para sonar concreto. Si falta un dato, pregunta al usuario o déjalo fuera. No uses marcadores tipo `[insertar aquí]` ni `XXXX`.
- No prometas que el texto es "indetectable". Ninguna señal prueba por sí sola el uso de IA, y los detectores fallan mucho.
- Escribe en el idioma pedido. Los patrones de abajo se dan en inglés (origen) con su equivalente en español; evita ambos.

## Flujo

1. Aclara lo mínimo: tema, público, extensión y fuentes disponibles. Si el usuario ya dio el borrador, reescríbelo; si no, redacta.
2. Redacta con las reglas de abajo.
3. **Revisión final antes de entregar:** recorre la lista de rasgos y elimina cada coincidencia. Si no tienes datos suficientes para ser específico, dilo en una línea en vez de rellenar.
4. Entrega el texto limpio, sin preámbulo ni oferta de ayuda al final.

## Qué evitar

### Contenido
- **Importancia inflada:** "marcó un momento clave", "sentó las bases", "pivotal", "crucial", "subraya su importancia", "legado duradero", "es un testimonio de", "stands as". Di qué pasó y deja que el hecho pese.
- **Notoriedad por listado de medios:** "aparecido en X, Y y otros medios". Cita una fuente concreta o nada.
- **Análisis superficial con gerundios al final:** "...reflejando su relevancia continua", "destacando", "contribuyendo a". Cada afirmación de impacto necesita sustento; si no, bórrala.
- **Conexiones vagas:** "asociado con", "vinculado a", "en relación con". Escribe la relación real.
- **Atribuciones vagas:** "los expertos señalan", "se ha interpretado ampliamente", "los críticos". Nombra quién lo dijo y dónde, o elimina la frase.
- **Sección formulaica de desafíos:** "A pesar de estos desafíos, ... el futuro luce prometedor". Sin cierre optimista de manual ni "Perspectivas futuras" por inercia.
- **Secciones de "Premios y reconocimientos"** puestas por reflejo.
- **Énfasis en fuentes primarias o bases de datos:** "el sitio registra/identifica que...". Informa el hecho, no el registro.
- **Tono promocional (turismo/folleto):** "enclavado en el corazón de", "vibrante", "rico patrimonio", "renombrado", "innovador", "boasts a", "compromiso con", "experiencias de valor". Usa descripción neutral y factual.
- **Descargos sobre fuentes (rasgo más frecuente actualmente):** "los detalles específicos son limitados", "no está ampliamente documentado", "según la información disponible", "no establece por sí solo". Si no hay sustento, omite la afirmación en lugar de especular sobre lo que no encontraste.
- **Avisos didácticos:** "es importante señalar que", "es crucial diferenciar", consejos a un lector imaginario.
- **Encuadres correctivos recientes:** "debe tratarse como... y no como...", "no debe confundirse con".
- **Aviso de fecha de corte:** "hasta mi última actualización". Nunca.
- **Resúmenes y conclusiones de relleno:** "En resumen", "En conclusión", "En general", un párrafo final que repite lo dicho. Termina con información nueva o termina antes.

### Lenguaje y gramática
- **Vocabulario sobreusado.** Evita agruparlo; donde aparece una, suelen venir otras:
  - 2023–2024: additionally/además, delve/profundizar, crucial, pivotal/fundamental, tapestry/tapiz, testament/testimonio, intricate/intrincado, vibrant/vibrante, underscore/subrayar, valuable, enduring/perdurable.
  - 2024–2026: align with/alinearse con, enhance/potenciar, fostering/fomentar, highlighting/destacar, showcasing/mostrar, emphasizing/enfatizar.
  - 2026 en adelante: challenge/desafío, leverage/aprovechar, multifaceted/multifacético, prioritize/priorizar, quietly, universally.
  - Grok: causal, empirical, correlate.
  - Una palabra no está prohibida por sí sola (puede usarse en su sentido literal); el problema es la acumulación y el uso decorativo.
- **Evitar el verbo "ser/estar/haber/tener":** "sirve como", "se erige como", "cuenta con", "alberga", "presenta", "boasts". Usa "es", "son", "hay", "tiene", y verbos simples: "usó" en vez de "utilizó", "murió" en vez de "falleció".
- **Paralelismos negativos:** "no solo X, sino también Y", "no es X, sino Y", "en lugar de...". No corrijas ideas erróneas que nadie tenía; afirma directamente lo que es.
- **Definir el término en vez del tema:** "X se refiere a...". Empieza con una frase natural sobre el sujeto.
- **Regla de tres:** listas de tres adjetivos o frases por ritmo. Lista solo lo que los hechos respaldan, sea uno, dos o cuatro.
- **Variación elegante:** no rotes sinónimos para el mismo referente ("los artistas disidentes", "las restricciones soviéticas", "su creatividad"). Repite el nombre claro.
- **Frases cortas y puntuación uniforme** como único recurso (tendencia de modelos recientes): varía la longitud y la estructura de forma natural.

### Estilo y formato
- **Markdown en texto que no lo requiere:** `**negritas**` en la prosa, `#` en encabezados de textos planos, `---` como separadores, triple acento grave. Si el destino es un documento (Docs, Word), usa su formato nativo, no sintaxis Markdown suelta.
- **Negritas en exceso** y **listas con etiqueta en negrita al inicio de cada ítem** ("**Rendimiento:** ..."). Prefiere prosa.
- **Encabezados en Title Case:** usa mayúscula solo en la primera palabra (y nombres propios).
- **Niveles de encabezado incorrectos:** un solo título principal y subniveles coherentes.
- **Emoji** al inicio de títulos o viñetas.
- **Comillas y apóstrofos curvos** (“ ” ’) donde el entorno usa rectos; sé consistente con el formato del destino.
- **Rayas largas (—):** no las uses como muletilla de "efecto de venta" ni con espacios a ambos lados. Elige coma, paréntesis, dos puntos o punto según la oración. Tampoco las sustituyas todas por comas mecánicamente.
- **Etiquetas de chatbot:** "Recomendado:", opciones numeradas, "Aquí tienes...".

### Comunicación dirigida al usuario (nunca en el texto final)
- "¡Claro!", "Espero que esto ayude", "¿Quieres que...?", "avísame si...", "Como modelo de lenguaje...", "Lo siento", disculpas, ofertas de ayuda, notas como "elimina esta sección antes de enviar".
- Marcadores sin rellenar: `[Título del artículo]`, `[Nombre del fundador]`, `2025-XX-XX`, `INSERTAR_URL`, ejemplo.com.
- Texto cortado a mitad de frase.
- Autorreferencias ("me comprometo a...") y garantías de haber seguido normas ("asegurando que cumple con las directrices").

### Citas y referencias (si el documento las lleva)
- Solo incluye fuentes reales y verificadas; cada enlace, DOI o ISBN debe existir y corresponder a lo que respalda.
- Libros con número de página cuando se citen para una afirmación concreta.
- Sin parámetros de rastreo (`utm_source=chatgpt.com`, `utm_source=openai`, `referrer=grok.com`) ni caracteres residuales como ↩ ni restos como `contentReference[oaicite:1]`.
- Fecha de acceso coherente con la fecha real del documento. Referencias definidas y usadas.

## Cómo suena humano (de verdad)

- Datos concretos y poco comunes en vez de descripciones generales halagadoras.
- Posiciones, matices y ritmo irregulares propios del tema; una opinión del autor solo si el usuario la tiene.
- Verbos simples, oraciones de longitud variada, sin simetría forzada.
- El registro que corresponda al público; no mezcles lo casual y lo formal por azar, pero tampoco "limpies" el texto hasta dejarlo sin personalidad.

## Señales que NO son prueba de IA (no las "corrijas" por sí solas)

Gramática perfecta, mezcla de registros formal e informal, prosa sobria o académica, conectores aislados como "además" o "por lo tanto", contenido sin fuentes, HTML o sintaxis rara por extensiones del navegador. Reescribe solo si hay un problema real de claridad o sustento.

## Salida

Entrega solo el documento final. Si quedaron datos faltantes que impidieron ser específico, añade al final del mensaje (fuera del documento) una línea con lo que necesitas del usuario.
