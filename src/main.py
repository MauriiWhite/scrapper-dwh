from sqlalchemy.exc import IntegrityError
from colorama import Fore, Style

from database.conection import Base, engine, SessionLocal
from utils.loads import load_data_to_db
from utils.mappers import map_to_product, map_to_branch, map_to_customer, map_to_sales
from utils.transforms import (
    transform_csv_products,
    transform_json_branches,
    transform_xlsx_customers,
    transform_xml_sales,
)

import models.database


def main():
    Base.metadata.create_all(bind=engine)

    try:
        with SessionLocal() as session:
            load_data_to_db(
                session,
                transform_xlsx_customers("data/customers.xlsx"),
                map_to_customer,
            )
            load_data_to_db(
                session, transform_json_branches("data/branches.json"), map_to_branch
            )
            load_data_to_db(
                session, transform_csv_products("data/products.csv"), map_to_product
            )
            load_data_to_db(
                session, transform_xml_sales("data/sales.xml"), map_to_sales
            )
            session.commit()
            print(
                f"{Fore.GREEN}{Style.BRIGHT}\u2713 | Datos insertados exitosamente.{Style.RESET_ALL}"
            )

    except IntegrityError:
        print(
            f"{Fore.RED}{Style.BRIGHT}\u2A2F | Datos anteriormente insertados.{Style.RESET_ALL}"
        )
        session.rollback()


if __name__ == "__main__":
    main()
