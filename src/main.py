from time import time
from colorama import Fore, Style

from models.product_response import ProductResponse
from mappers.product_mapper import ProductMapper
from scrappers.scrapper_products import ScrapperProducts


def main():
    scrapper = ScrapperProducts(
        base_url="https://apps.lider.cl/catalogo/bff/category",
        headers={
            "tenant": "catalogo",
            "x-channel": "BuySmart",
            "content-type": "application/json",
        },
        method="post",
        json={
            "categories": "Computación",
            "page": 1,
            "hitsPerPage": 100,
        },
        entity_response=ProductResponse,
        mapper=ProductMapper,
    )
    print(
        f"{Fore.GREEN}{Style.BRIGHT}Initializing Scrapper...{Style.RESET_ALL}{Fore.RESET}"
    )

    for i in range(1, 13):
        start_time = time()
        items = scrapper.scrap(page=i)
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
