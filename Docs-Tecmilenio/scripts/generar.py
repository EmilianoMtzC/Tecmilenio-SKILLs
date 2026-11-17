#!/usr/bin/env python3
"""Llena la plantilla de Tecmilenio y genera .docx (el .pdf es opcional con --pdf).

Uso:
  generar.py --curso "Nombre" --actividad 3 --titulo "Título" [--profesor "X"]
             [--cuerpo archivo.txt] [--salida carpeta] [--pdf]

Cuerpo: párrafos separados por línea en blanco; "## " = subtítulo en negritas;
"- " = viñeta. Solo usa la librería estándar.
"""
import argparse, datetime, re, shutil, subprocess, sys, zipfile
from pathlib import Path
from xml.sax.saxutils import escape

RAIZ = Path(__file__).resolve().parent.parent
PLANTILLA = RAIZ / "assets" / "plantilla.docx"
CURSOS = RAIZ / "cursos.md"
NOMBRE = "Jesús Emiliano Martínez Ceja"
MATRICULA = "AL07108460"
MESES = ["enero","febrero","marzo","abril","mayo","junio","julio","agosto",
         "septiembre","octubre","noviembre","diciembre"]
F = '<w:rFonts w:ascii="Calibri" w:cs="Calibri" w:eastAsia="Calibri" w:hAnsi="Calibri"/>'

def filas():
    out = []
    for l in CURSOS.read_text(encoding="utf8").splitlines():
        c = [x.strip() for x in l.strip().strip("|").split("|")]
        if l.startswith("|") and len(c) == 3 and c[0] not in ("Curso",) and not set(c[0]) <= set("-"):
            out.append(c)
    return out

def buscar_curso(curso):
    """Devuelve (nombre a mostrar en el documento, profesor) o None."""
    for c in filas():
        if curso.lower() in (c[0].lower(), c[1].lower()):
            return (c[1] or c[0]), c[2]
    return None

def guardar_curso(curso, prof, abrev=""):
    f = [c for c in filas() if curso.lower() not in (c[0].lower(), c[1].lower())]
    viejo = buscar_curso(curso)
    f.append([curso, abrev or (viejo[0] if viejo and viejo[0] != curso else ""), prof])
    CURSOS.write_text("# Cursos y profesores\n\nTabla que usa la skill.\n"
                      "\"Nombre en el documento\" es como aparece en el campo del curso (vacío = nombre completo).\n\n"
                      "| Curso | Nombre en el documento | Profesor |\n|---|---|---|\n" +
                      "".join(f"| {a} | {b} | {c} |\n" for a, b, c in f), encoding="utf8")

def run(texto, negrita=False):
    b = '<w:b w:val="1"/><w:bCs w:val="1"/>' if negrita else ""
    return (f'<w:r><w:rPr>{F}{b}</w:rPr>'
            f'<w:t xml:space="preserve">{escape(texto)}</w:t></w:r>')

def poner_valor(xml, para_id, valor):
    """Agrega el valor justo después del run de la etiqueta en ese párrafo."""
    pat = re.compile(r'(<w:p [^>]*w14:paraId="%s".*?<w:t[^>]*>[^<]*</w:t></w:r>)' % para_id, re.S)
    if not pat.search(xml):
        sys.exit(f"No encontré el párrafo {para_id} en la plantilla")
    return pat.sub(lambda m: m.group(1) + run(valor), xml, count=1)

def cuerpo_xml(texto):
    out = []
    for bloque in re.split(r"\n\s*\n", texto.strip()):
        for l in bloque.splitlines():
            l = l.rstrip()
            if not l:
                continue
            if l.startswith("## "):
                r, sp = run(l[3:], True), 'w:before="200" w:after="80"'
            elif l.startswith("- "):
                r, sp = run("•  " + l[2:]), 'w:after="60"'
            else:
                r, sp = run(l), 'w:after="160"'
            ind = ('<w:ind w:left="360" w:right="0" w:hanging="260"/>' if l.startswith("- ")
                   else '<w:ind w:left="0" w:right="0" w:firstLine="0"/>')
            out.append(f'<w:p><w:pPr><w:spacing {sp} w:line="276" w:lineRule="auto"/>{ind}'
                       f'<w:jc w:val="both"/></w:pPr>{r}</w:p>')
    return "".join(out)

def main():
    a = argparse.ArgumentParser()
    a.add_argument("--curso", required=True)
    a.add_argument("--actividad", required=True)
    a.add_argument("--titulo", required=True)
    a.add_argument("--profesor")
    a.add_argument("--abreviatura", default="")
    a.add_argument("--cuerpo")
    a.add_argument("--salida", default=".")
    a.add_argument("--pdf", action="store_true", help="solo para revisar el diseño; el entregable es el .docx")
    a = a.parse_args()

    hallado = buscar_curso(a.curso)
    prof = a.profesor or (hallado[1] if hallado else None)
    if not prof:
        sys.exit(f"PROFESOR_DESCONOCIDO: '{a.curso}' no está en cursos.md; pide el nombre del profesor.")
    if a.profesor or a.abreviatura:
        guardar_curso(a.curso, prof, a.abreviatura)
    hallado = buscar_curso(a.curso)
    curso_doc = hallado[0] if hallado else a.curso

    hoy = datetime.date.today()
    fecha = f"{hoy.day} de {MESES[hoy.month-1]} de {hoy.year}"
    cuerpo = Path(a.cuerpo).read_text(encoding="utf8") if a.cuerpo else ""

    with zipfile.ZipFile(PLANTILLA) as z:
        xml = z.read("word/document.xml").decode("utf8")
        for pid, v in [("00000002", NOMBRE), ("00000005", " " + MATRICULA),
                       ("00000006", curso_doc), ("00000007", prof),
                       ("0000000A", a.actividad),
                       ("0000000C", fecha)]:
            if v:
                xml = poner_valor(xml, pid, v)
        # se elimina la celda "Módulo" y "Actividad" ocupa toda la fila
        xml, n = re.subn(r'<w:tc>(?:(?!</w:tc>).)*?w14:paraId="00000009".*?</w:tc>', "", xml, count=1, flags=re.S)
        xml = re.sub(r'<w:gridSpan w:val="2"/>(?=(?:(?!</w:tc>).)*?w14:paraId="0000000A")', '<w:gridSpan w:val="3"/>', xml, count=1, flags=re.S)
        # título: la plantilla dice "Actividad -"; se conserva y se agrega el título tal cual
        xml = xml.replace("Actividad -</w:t>", escape(f"Actividad - {a.titulo}") + "</w:t>", 1)
        # cuerpo: reemplaza el último párrafo vacío (antes de sectPr)
        if cuerpo:
            xml = re.sub(r'<w:p [^>]*w14:paraId="00000010".*?</w:p>', lambda m: cuerpo_xml(cuerpo), xml, count=1, flags=re.S)
        nombre = re.sub(r'[\\/:*?"<>|]', "", f"Actividad {a.actividad} - {a.titulo}")
        salida = Path(a.salida).expanduser().resolve(); salida.mkdir(parents=True, exist_ok=True)
        destino = salida / f"{nombre}.docx"
        with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as o:
            for i in z.infolist():
                o.writestr(i, xml.encode("utf8") if i.filename == "word/document.xml" else z.read(i.filename))
    print(destino)

    if a.pdf:
        # La vista previa va a una carpeta aparte; NUNCA junto al .docx entregable.
        prev = Path.home() / ".cache" / "docs-tecmilenio-preview"
        shutil.rmtree(prev, ignore_errors=True); prev.mkdir(parents=True)
        cmd = (["soffice"] if shutil.which("soffice") else
               ["flatpak", "run", "org.libreoffice.LibreOffice"])
        r = subprocess.run(cmd + ["--headless", "--convert-to", "pdf", "--outdir", str(prev), str(destino)],
                           capture_output=True, text=True)
        pdf = prev / (destino.stem + ".pdf")
        print("Vista previa (temporal):", pdf if pdf.exists() else f"PDF no generado: {r.stderr.strip()}")

main()
