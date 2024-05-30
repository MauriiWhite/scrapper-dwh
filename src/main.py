import requests

from time import time
from typing import List
from colorama import Fore, Style

from entities.product import Product
from models.product_response import ProductResponse
from mappers.product_mapper import ProductMapper


class ScrapperException(Exception):
    def __init__(self, message: str):
        super().__init__(message)

    def __str__(self) -> str:
        return self.message


class Scrapper:
    def __init__(self, url: str):
        self.__url = url

    def _json_to_products(self, json: dict) -> List[Product]:
        if json.get("redirectUrl") is not None:
            raise ScrapperException(f"Scrapper blocked by request")

        product_response = ProductResponse.from_json(json)
        products = [
            ProductMapper.product_to_entity(product)
            for product in product_response.results
        ]
        return products

    def scrap(self, page: int = 1) -> List[Product]:
        response = requests.post(
            url=self.__url,
            headers={
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "tenant": "catalogo",
                "x-channel": "BuySmart",
                "content-type": "application/json",
            },
            json={
                "categories": "Computación",
                "page": page,
                "facets": [],
                "sortBy": "",
                "hitsPerPage": 100,
            },
        )
        return self._json_to_products(response.json())


def main():
    scrapper = Scrapper("https://apps.lider.cl/catalogo/bff/category")

    print(
        f"{Fore.GREEN}{Style.BRIGHT}Initializing Scrapper...{Style.RESET_ALL}{Fore.RESET}"
    )

    for i in range(1, 13):
        start_time = time()
        items = scrapper.scrap(i)
        if len(items) == 0:
            print(
                f"{Fore.GREEN}All pages scraped in {Style.BRIGHT}{i - 1} pages{Fore.RESET}{Style.RESET_ALL}"
            )
            break

        print(
            f"{Fore.CYAN}Page {i}{Fore.RESET} | {Fore.GREEN}Total {len(items)}{Fore.RESET} | {Fore.MAGENTA}{time() - start_time:.2f}s{Fore.RESET}"
        )


if __name__ == "__main__":
    main()
