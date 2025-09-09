import os
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from pypdf import PdfReader, PdfWriter

PLANTILLA = "plantilla/Plantilla-Constancia.pdf"
EXCEL_DATOS = "datos/base_datos.xlsx"
CARPETA_SALIDA = "salida/certificados"

os.makedirs(CARPETA_SALIDA, exist_ok=True)

def leer_excel(ruta_archivo):
    df = pd.read_excel(ruta_archivo)
    columnas = ["Nombre", "Motivo", "Fecha"]
    for col in columnas:
        if col not in df.columns:
            raise ValueError(f"Falta columna: {col}")
    return df.to_dict(orient="records")

def generar_certificado(participante):
    page_size = landscape(letter)
    width, height = page_size
    c = canvas.Canvas("temp.pdf", pagesize=page_size)

    y_nombre = 330
    y_motivo = 290
    y_fecha = 250
    x_derecha = width - 50  

    nombre_texto = participante["Nombre"]
    c.setFont("Helvetica-Bold", 36)
    c.drawRightString(x_derecha, y_nombre, nombre_texto)

    nombre_width = c.stringWidth(nombre_texto, "Helvetica-Bold", 36)
    x_medio_nombre = x_derecha - nombre_width / 2

    c.setFont("Helvetica", 24)
    c.drawCentredString(x_medio_nombre, y_motivo, participante["Motivo"])

    c.setFont("Helvetica", 20)
    c.drawCentredString(x_medio_nombre, y_fecha, participante["Fecha"])

    c.save()

    template_pdf = PdfReader(PLANTILLA)
    temp_pdf = PdfReader("temp.pdf")
    output = PdfWriter()

    page = template_pdf.pages[0]
    page.merge_page(temp_pdf.pages[0])
    output.add_page(page)

    nombre_archivo = os.path.join(
        CARPETA_SALIDA, f"{participante['Nombre'].replace(' ', '_')}.pdf"
    )
    with open(nombre_archivo, "wb") as f:
        output.write(f)

    print(f"Generado: {nombre_archivo}")

if __name__ == "__main__":
    participantes = leer_excel(EXCEL_DATOS)
    for p in participantes:
        generar_certificado(p)
