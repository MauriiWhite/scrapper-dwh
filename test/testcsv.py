import csv
import json


# Cargar datos desde un archivo JSON (o una cadena JSON)
with open("data\products.json", "r") as f:
    datos_json = json.load(f)

encabezados = datos_json[0].keys()

# Escribir datos en un archivo CSV
with open("products.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=encabezados)
    writer.writeheader()
    writer.writerows(datos_json)
