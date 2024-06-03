import json
import xml.etree.ElementTree as ET


# Función para convertir un diccionario a XML
def dict_to_xml(tag, d):
    """
    Turn a simple dict of key/value pairs into XML
    """
    elem = ET.Element(tag)
    for key, val in d.items():
        child = ET.Element(key)
        child.text = str(val)
        elem.append(child)
    return elem


# Cargar datos desde un archivo JSON (o una cadena JSON)
with open("data\sales.json", "r") as f:
    datos_json = json.load(f)

# Crear el elemento raíz del XML
root = ET.Element("sales")

# Convertir cada entrada del JSON en un elemento XML
for entry in datos_json:
    elem = dict_to_xml("item", entry)
    root.append(elem)

# Crear un árbol XML
tree = ET.ElementTree(root)

# Escribir el árbol XML en un archivo
nombre_archivo_xml = "sales.xml"
tree.write(nombre_archivo_xml, encoding="utf-8", xml_declaration=True)

print(f"Se han guardado los datos en {nombre_archivo_xml}")
