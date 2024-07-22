from sqlalchemy.exc import IntegrityError

from utils.loads import load_data
from utils.messages import print_msg
from database.conection import Base, engine, SessionLocal
from utils.transforms import csv_products, json_branches, xlsx_customers, xml_sales
from utils.mappers import map_to_product, map_to_branch, map_to_customer, map_to_sales

import models.database


def main():
    Base.metadata.create_all(bind=engine)
    print_msg("Modelos creados 'models.database'")

    try:
        with SessionLocal() as session:
            load_data(session, xlsx_customers("data/customers.xlsx"), map_to_customer)
            load_data(session, json_branches("data/branches.json"), map_to_branch)
            load_data(session, csv_products("data/products.csv"), map_to_product)
            load_data(session, xml_sales("data/sales.xml"), map_to_sales)
            session.commit()
            print_msg("Datos insertados exitosamente")
    except IntegrityError:
        print_msg("Datos anteriormente insertados", is_error=True)
        session.rollback()
    finally:
        session.close()


if __name__ == "__main__":
    main()
    import graphics.statistics
