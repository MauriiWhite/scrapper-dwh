from datetime import date
from sqlalchemy import func

from database.conection import session
from models.database import Product, Sales, Branch, Customer


total_products_sold = (
    session.query(Product.brand, Sales.quantity)
    .join(Sales)
    .group_by(Product.brand)
    .all()
)

revenues_per_branch = (
    session.query(Branch.branch_name, func.sum(Sales.final_amount))
    .join(Sales)
    .group_by(Branch.branch_name)
    .all()
)

customers_by_gender = (
    session.query(Customer.gender, func.count(Customer.customer_id))
    .group_by(Customer.gender)
    .all()
)

avg_discount_per_product = (
    session.query(Product.brand, func.avg(Product.discount))
    .group_by(Product.brand)
    .all()
)

sales_by_date = (
    session.query(Sales.sale_date, func.sum(Sales.final_amount))
    .group_by(Sales.sale_date)
    .all()
)

customers_age = session.query(
    date.today().year - func.extract("year", Customer.date_birth)
).all()
