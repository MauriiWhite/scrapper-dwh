import json
import pandas as pd

# Cargar datos desde un archivo JSON (o una cadena JSON)
with open("data\customers.json", "r") as f:
    datos_json = json.load(f)

# Crear un DataFrame de pandas
df = pd.DataFrame(datos_json)

# Escribir el DataFrame en un archivo Excel
nombre_archivo_excel = "customers.xlsx"
df.to_excel(nombre_archivo_excel, index=False, engine="openpyxl")

print(f"Se han guardado los datos en {nombre_archivo_excel}")
