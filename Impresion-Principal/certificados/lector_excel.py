import pandas as pd

def leer_excel(ruta_archivo):

    df = pd.read_excel(ruta_archivo)
    columnas = ["Nombre", "Motivo", "Fecha"]

    for col in columnas:
        if col not in df.columns:
            raise ValueError(f"Falta columna: {col}")

    return df.to_dict(orient="records")
