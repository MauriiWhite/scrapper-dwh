from pprint import pformat
from typing import Any, TypeVar

T = TypeVar("T")


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


class Product:
    COUNTER = 0

    def __init__(
        self,
        # code: str,
        brand: str,
        description: str,
        # image: str,
        # thumbnail: str,
        # sku: str,
        # link: str,
        price: int,
        reference: int,
        discount: int,
    ):
        # self.__code = code
        self.__brand = brand
        self.__description = description
        # self.__image = image
        # self.__thumbnail = thumbnail
        # self.__sku = sku
        # self.__link = link
        self.__price = price
        self.__reference = reference
        self.__discount = discount

        Product.COUNTER += 1
        self.__counter = Product.COUNTER

    # @property
    # def code(self):
    #     return self.__code

    @property
    def brand(self):
        return self.__brand

    @property
    def description(self):
        return self.__description

    # @property
    # def image(self):
    #     return self.__image

    # @property
    # def thumbnail(self):
    #     return self.__thumbnail

    # @property
    # def sku(self):
    #     return self.__sku

    # @property
    # def link(self):
    #     return self.__link

    @property
    def price(self):
        return self.__price

    @property
    def reference(self):
        return self.__reference

    @property
    def discount(self):
        return self.__discount

    def to_dict(self) -> dict:
        result: dict = {}
        # result["code"] = from_str(self.code)
        result["brand"] = from_str(self.brand)
        result["description"] = from_str(self.description)
        # result["image"] = from_str(self.image)
        # result["thumbnail"] = from_str(self.thumbnail)
        # result["sku"] = from_str(self.sku)
        # result["link"] = from_str(self.link)
        result["price"] = from_int(self.price)
        result["reference"] = from_int(self.reference)
        result["discount"] = from_int(self.discount)
        return result

    def __str__(self) -> str:
        return f"\n{self.__counter} | {pformat(self.to_dict(), sort_dicts=False)}"
