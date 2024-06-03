from json import dump, load
from typing import List, Dict, Union, Optional, NoReturn

Item = Dict[str, Union[int, str, float]]
Data = List[Item]


def load_json(file_path: str) -> Data:
    with open(file_path, "r", encoding="utf-8") as file:
        return load(file)


def save_json(data: Data, file_path: str) -> NoReturn:
    with open(file_path, "w", encoding="utf-8") as file:
        dump(data, file, indent=2)


def get_product_by_id(products: Data, id: int) -> Optional[Item]:
    for product in products:
        if product["productID"] == id:
            return product
    return None


def update_sales_total(sales: Data, products: Data) -> None:
    for sale in sales:
        product = get_product_by_id(products, int(sale["productID"]))
        if product is not None:
            quantity = int(sale["quantity"])

            price = product["price"]
            discount = product["discount"]
            reference = product["reference"]

            sale["finalAmount"] = price * quantity
            sale["totalAmount"] = reference * quantity
            sale["discount"] = discount


if __name__ == "__main__":
    sales_file = "data/sales.json"
    products_file = "data/products.json"

    sales = load_json(sales_file)
    products = load_json(products_file)

    update_sales_total(sales, products)
    save_json(sales, sales_file)
