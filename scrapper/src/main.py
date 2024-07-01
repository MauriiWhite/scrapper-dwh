from os import environ
from typing import List
from dotenv import load_dotenv

from entities.product import Product
from config.manager import JSONFileManager
from mappers.product_mapper import ProductMapper
from models.product_response import ProductResponse
from config.config import headers, json_schema, method
from scrappers.scrapper_products import ScrapperProducts

load_dotenv()

URL = environ.get("URL")


def main():
    scrapper = ScrapperProducts(
        base_url=URL,
        headers=headers,
        method=method,
        json=json_schema,
        entity_response=ProductResponse,
        mapper=ProductMapper,
    )

    manager = JSONFileManager("data", "products.json")

    for page in range(1, 12):
        result: List[Product] = scrapper.scrap(page=page)
        for product in result:
            manager.add_objects(product.to_dict())

    print(scrapper.total_time)


if __name__ == "__main__":
    main()
