from pathlib import Path
from json import dumps, load
from io import TextIOWrapper
from typing import List, Dict, NoReturn, Any


class JSONFileManager:
    def __init__(self, dirname: str, filename: str):
        self.__dirname = dirname
        self.__filename = filename
        self.__dir_file = (
            Path(__file__)
            .parent.parent.parent.parent.joinpath(self.__dirname)
            .joinpath(self.__filename)
        )

        self._create_file()

    def _create_file(self) -> NoReturn:
        try:
            with open(self.__dir_file, "w", encoding="utf-8") as file:
                file.write(dumps([]))
        except FileNotFoundError:
            print(f"Error: El directorio '{self.__dirname}' no se encuentra.")
        except Exception as e:
            print(f"Error inesperado: {e}")
        finally:
            file.close()

    def truncate_file(
        self, file: TextIOWrapper, content: List[Dict[str, Any]]
    ) -> NoReturn:
        file.seek(0)
        file.write(dumps(content, ensure_ascii=False))
        file.truncate()
        file.close()

    def add_objects(self, obj: Dict[str, Any]) -> NoReturn:
        with open(self.__dir_file, "r+", encoding="utf-8") as file:
            data = load(file)
            data.append(obj)
            self.truncate_file(file, data)


if __name__ == "__main__":
    json_manager = JSONFileManager()
    json_manager.create_file()

    obj_to_add = {"name": "Example Product", "price": 50}
    json_manager.add_objects(obj_to_add)
