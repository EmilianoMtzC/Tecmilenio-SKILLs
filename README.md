# Tecmilenio SKILLs

Dos skills de [Claude Code](https://claude.com/claude-code) para hacer las entregas de la universidad:

| Skill | Qué hace | Se activa con |
|---|---|---|
| **Docs-Tecmilenio** | Genera el `.docx` con la plantilla oficial de entrega de actividad (logo, tabla de datos, pie con número de página). | Un mensaje que empiece con **"Redacta un documento para la uni"** |
| **AI-Humanizer** | Redacta o reescribe textos sin los rasgos típicos de la escritura generada por IA. | **"Crea documento humanizado"** |

Docs-Tecmilenio usa AI-Humanizer automáticamente antes de redactar, así que no tienes que pedirlo aparte.

## Requisitos

- Claude Code instalado.
- `python3` (el script solo usa la biblioteca estándar).
- Opcional: LibreOffice (`soffice`), solo para generar una vista previa en PDF.

## Instalación

```bash
git clone https://github.com/EmilianoMtzC/Tecmilenio-SKILLs ~/tecmilenio-skills
ln -s ~/tecmilenio-skills/AI-Humanizer ~/.claude/skills/AI-Humanizer
ln -s ~/tecmilenio-skills/Docs-Tecmilenio ~/.claude/skills/Docs-Tecmilenio
```

También puedes copiar las dos carpetas directamente a `~/.claude/skills/`.
Para actualizar, haz `git pull` dentro de `~/tecmilenio-skills`.

## Uso

Escribe en Claude Code un mensaje así:

```
Redacta un documento para la uni. Curso: Metodologías Ágiles.
Actividad 3: "Marco de trabajo Scrum".
Tema: explica los roles, eventos y artefactos de Scrum.
```

Claude necesita de ti:

- **Curso** (aparece en el campo "Nombre del curso").
- **Número de actividad** (solo el número).
- **Título** de la actividad (queda como `Actividad - <Título>`).
- **Tema o contenido** a redactar.

El resultado es `Actividad N - Título.docx` en el directorio de trabajo (o en la carpeta que indiques). La fecha es siempre la del día.

## Primer uso: tus datos

Cada persona tiene sus propios datos. No vienen en el repositorio y se piden una sola vez:

- **Nombre y matrícula.** Si falta `perfil.md`, Claude te los pregunta y los guarda.
- **Profesor.** Si el curso no está en `cursos.md`, Claude pregunta el profesor y lo guarda. Después ya no vuelve a preguntar.
- **Abreviatura del curso** (opcional). Pídela si el nombre es largo, por ejemplo "Met. Ágiles". Queda guardada para ese curso.
- **Cambiar de profesor.** Dile a Claude el nuevo profesor del curso y se actualiza.

Estos archivos viven en `Docs-Tecmilenio/` y están en `.gitignore`, así que nunca se suben:

| Archivo | Contenido |
|---|---|
| `perfil.md` | Nombre y matrícula |
| `cursos.md` | Tabla de cursos, abreviaturas y profesores |
| `plantilla-personal.docx` | Tu plantilla propia (si usas una) |

## Cambiar la plantilla

Si quieres otro diseño, pídele a Claude que use tu plantilla (dale la ruta del `.docx`) o ejecuta:

```bash
python3 -I ~/.claude/skills/Docs-Tecmilenio/scripts/generar.py --plantilla ruta/mi-plantilla.docx
```

Reglas para que funcione:

- Parte de una copia de `Docs-Tecmilenio/assets/plantilla.docx`.
- Puedes cambiar logo, fuentes, colores y encabezado.
- **No borres** la tabla de datos ni el párrafo vacío final: el script los llena.
- Si falta algo, el script avisa con `PLANTILLA_INVALIDA` y no instala nada.

Para volver a la plantilla oficial:

```bash
python3 -I ~/.claude/skills/Docs-Tecmilenio/scripts/generar.py --restaurar-plantilla
```

## Uso directo del script (opcional)

```bash
python3 -I ~/.claude/skills/Docs-Tecmilenio/scripts/generar.py \
  --curso "CURSO" --actividad N --titulo "TÍTULO" \
  [--nombre "NOMBRE" --matricula "MAT"] [--profesor "PROF"] [--abreviatura "ABREV"] \
  --cuerpo cuerpo.txt --salida carpeta/
```

El archivo `cuerpo.txt` lleva párrafos separados por una línea en blanco, `## Subtítulo` para subtítulos y `- ` para viñetas. Con `--pdf` se genera una vista previa temporal en `~/.cache/docs-tecmilenio-preview/` (nunca junto al `.docx`).

## Estructura

```
AI-Humanizer/SKILL.md
Docs-Tecmilenio/
├── SKILL.md
├── assets/plantilla.docx      # plantilla oficial
└── scripts/generar.py         # llena la plantilla y crea el .docx
```
