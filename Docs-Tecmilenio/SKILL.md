---
name: Docs-Tecmilenio
description: Genera documentos de la Universidad Tecmilenio (.docx) con la plantilla oficial de entrega de actividad (logo, tabla de datos, pie con número de página). Úsala SIEMPRE que la petición del usuario empiece con "Redacta un documento para la uni".
---

# Docs-Tecmilenio

Se activa cuando el mensaje empieza con **"Redacta un documento para la uni"**.

## Combinación con AI-Humanizer
Esta skill SIEMPRE se combina con **AI-Humanizer**: en cuanto se active, invoca también la skill `AI-Humanizer` (con la herramienta Skill) **antes de redactar**, y escribe el cuerpo del documento siguiendo sus reglas.

## Datos fijos
- Nombre y matrícula: salen de `perfil.md` (personal, en `.gitignore`, no viene en el repo). Si no existe, el script imprime `PERFIL_DESCONOCIDO`: pregunta nombre completo y matrícula y pásalos con `--nombre` y `--matricula`; el script los guarda solo para la próxima vez.
- Fecha: siempre la actual (el script la pone)
- Plantilla: `assets/plantilla.docx` (copia exacta de "Plantilla entrega de Actividad.docx"; trae logo, encabezado, tabla y pie con número de página). No se modifica; el script la llena.
- **Plantilla propia (opcional):** si el usuario quiere otra plantilla, pásala con `--plantilla ruta.docx` (puede ir sola, sin curso). El script valida que conserve los párrafos que llena (`PLANTILLA_INVALIDA` si faltan; debe partir de una copia de `assets/plantilla.docx` sin borrar la tabla de datos ni el párrafo final) y la guarda como `plantilla-personal.docx` (en `.gitignore`), que desde entonces tiene prioridad. `--restaurar-plantilla` vuelve a la oficial.

## Datos que da el usuario en cada petición
- **Curso** → "Nombre del curso". El profesor se busca en `cursos.md`.
- **Número de actividad** → campo "Actividad:" (solo el número).
- **Título** de la actividad: se escribe tal cual lo da el usuario bajo la tabla, tras el texto fijo de la plantilla: `Actividad - <Título>`.
- El tema/contenido a redactar.

## Tabla curso ↔ profesor (`cursos.md`)
- `cursos.md` es personal de cada usuario: no viene en el repo (está en `.gitignore`) y el script lo crea solo la primera vez que se pasa `--profesor`. Si no existe, el curso se considera desconocido.
- Si el curso ya está en la tabla, no preguntes el profesor.
- Si no está, pregunta el nombre del profesor y pásalo con `--profesor`; el script lo guarda solo.
- Si el usuario da un profesor distinto para un curso existente, `--profesor` lo actualiza.

- Si el usuario pide abreviar el curso en el documento, pásalo con `--abreviatura`; queda guardado y se usa siempre en ese curso (el campo del documento muestra la abreviatura).

## Pasos
1. Invoca AI-Humanizer y redacta el contenido (ya humanizado) en un archivo de texto temporal (scratchpad). Formato: párrafos separados por línea en blanco, `## Subtítulo` para subtítulos, `- ` para viñetas. Sin Markdown adicional.
2. Ejecuta:
   ```
   python3 -I ~/.claude/skills/Docs-Tecmilenio/scripts/generar.py \
     --curso "CURSO" --actividad N --titulo "TÍTULO" \
     [--nombre "NOMBRE" --matricula "MAT"] [--profesor "PROF"] [--abreviatura "ABREV"] --cuerpo cuerpo.txt \
     --salida "<carpeta>"
   ```
   Carpeta de salida por defecto: el directorio de trabajo actual. Si el script imprime `PROFESOR_DESCONOCIDO`, pregunta el profesor y repite.
3. El entregable final es SIEMPRE el `.docx` (`Actividad N - Título.docx`); no entregues PDF. Para revisar el diseño, genera una vista previa con `--pdf` (se guarda aparte en `~/.cache/docs-tecmilenio-preview/`, nunca junto al .docx), mírala con `pdftoppm -png -r 70 archivo.pdf /ruta/scratch/pg` (logo, tabla, pie con número) y borra esa carpeta de vista previa al terminar; en la carpeta final debe quedar solo el .docx. Jamás copies ni dejes un .pdf en la carpeta del usuario.
4. Informa al usuario la ruta del .docx.

## Notas
- La plantilla ya no lleva el campo "Módulo": el script lo elimina y "Actividad:" ocupa toda la fila.
