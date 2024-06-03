from typing import List
from utils.schemas.abc import EntityResponse

from models.product_product import ProductProduct


class ProductResponse(EntityResponse):
    def __init__(self, results: List[ProductProduct]):
        self.__results = results

    @classmethod
    def from_json(cls, json: dict) -> "ProductResponse":
        return cls(
            results=[ProductProduct.from_dict(product) for product in json["products"]]
        )

    @property
    def results(self) -> List[ProductProduct]:
        return self.__results
