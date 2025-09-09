from lector_excel import leer_excel
from generador import generar_certificado

import os

os.makedirs("salida/certificados", exist_ok=True)

participantes = leer_excel("datos/base_datos.xlsx")

for persona in participantes:
    nombre_archivo = f"salida/certificados/{persona['Nombre'].replace(' ', '_')}.pdf"

    generar_certificado(
        persona
    )
