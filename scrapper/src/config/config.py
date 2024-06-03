from toml import load, TomlDecodeError

try:
    with open("config.toml", "r", encoding="utf-8") as f:
        config = load(f)
except FileNotFoundError:
    print("Error: El archivo 'config.toml' no se encontró.")
    config = None
except TomlDecodeError as e:
    print(f"Error al decodificar el archivo TOML: {e}")
    config = None
except Exception as e:
    print(f"Error inesperado: {e}")
    config = None

if config:
    try:
        scrapper = config["scrapper"]
        headers = scrapper["headers"]
        json_schema = scrapper["json"]
        method = scrapper["method"]
    except KeyError as e:
        print(f"Error: La clave {e} no se encuentra en el archivo 'config.toml'.")
    except Exception as e:
        print(f"Error inesperado al acceder a los datos del 'scrapper': {e}")
else:
    print("No se pudo cargar la configuración.")

if __name__ == "__main__":
    # Test config.py
    print(config)
