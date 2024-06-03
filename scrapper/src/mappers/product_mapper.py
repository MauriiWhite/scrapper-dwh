from utils.schemas.abc import Mapper

from entities.product import Product
from models.product_response import ProductProduct


class ProductMapper(Mapper):
    @staticmethod
    def to_entity(product: ProductProduct) -> Product:
        return Product(
            brand=product.brand,
            description=product.description,
            price=product.price.base_price_sales,
            reference=product.price.base_price_reference,
            discount=product.discount,
        )
