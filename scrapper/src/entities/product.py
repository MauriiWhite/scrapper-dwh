from pprint import pformat
from utils.schemas.abc import Entity


class Product(Entity):
    COUNTER = 0

    def __init__(
        self, brand: str, description: str, price: int, reference: int, discount: int
    ):
        self.__brand = brand
        self.__description = description
        self.__price = price
        self.__reference = reference
        self.__discount = discount

        Product.COUNTER += 1
        self.__counter = Product.COUNTER

    def to_dict(self) -> dict:
        result: dict = {}
        result["product_id"] = self.__counter
        result["brand"] = self.__brand
        result["description"] = self.__description
        result["price"] = self.__price
        result["reference"] = self.__reference
        result["discount"] = self.__discount
        return result

    def __str__(self) -> str:
        return f"\n{self.__counter} | {pformat(self.to_dict(), sort_dicts=False)}"
