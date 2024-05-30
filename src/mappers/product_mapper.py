from entities.product import Product
from models.product_response import ProductProduct


class ProductMapper:
    @staticmethod
    def product_to_entity(product: ProductProduct) -> Product:
        return Product(
            # code=product.id,
            brand=product.brand,
            description=product.description,
            # image=product.images.large_image,
            # thumbnail=product.images.small_image,
            # sku=product.sku,
            # link=f"https://www.lider.cl/product/{product.sku}",
            price=product.price.base_price_sales,
            reference=product.price.base_price_reference,
            discount=product.discount,
        )
