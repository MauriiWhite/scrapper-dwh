import matplotlib.pyplot as plt

from sqlalchemy import func
from database.conection import session
from models.database import Product, Sales, Branch, Customer

total_products_sold = (
    session.query(Product.brand, Sales.quantity)
    .join(Sales)
    .group_by(Product.brand)
    .all()
)

brands = [item[0] for item in total_products_sold]
quantities = [item[1] for item in total_products_sold]

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(brands, quantities, color="blue")
plt.xlabel("Marcas de Producto")
plt.ylabel("Cantidad Vendida")
plt.title("Total de Productos Vendidos por Marca")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# Consulta para obtener los ingresos por sucursal
revenues_per_branch = (
    session.query(Branch.branch_name, func.sum(Sales.final_amount))
    .join(Sales)
    .group_by(Branch.branch_name)
    .all()
)

# Preparar los datos para el gráfico
branches = [item[0] for item in revenues_per_branch]
revenues = [item[1] for item in revenues_per_branch]

# Crear el gráfico de barras horizontales
plt.figure(figsize=(10, 6))
plt.barh(branches, revenues, color="green")
plt.xlabel("Ingresos")
plt.ylabel("Sucursal")
plt.title("Ingresos por Sucursal")
plt.tight_layout()
plt.show()

# Consulta para obtener la cantidad de clientes por género
customers_by_gender = (
    session.query(Customer.gender, func.count(Customer.customer_id))
    .group_by(Customer.gender)
    .all()
)

# Preparar los datos para el gráfico de sectores (pie chart)
genders = [item[0] for item in customers_by_gender]
counts = [item[1] for item in customers_by_gender]

# Crear el gráfico de sectores
plt.figure(figsize=(8, 8))
plt.pie(
    counts,
    labels=genders,
    autopct="%1.1f%%",
    startangle=140,
    colors=["skyblue", "pink"],
)
plt.title("Distribución de Clientes por Género")
plt.axis("equal")
plt.show()


# Consulta para obtener el descuento promedio por producto
avg_discount_per_product = (
    session.query(Product.brand, func.avg(Product.discount))
    .group_by(Product.brand)
    .all()
)

# Preparar los datos para el gráfico de barras
brands = [item[0] for item in avg_discount_per_product]
avg_discounts = [item[1] for item in avg_discount_per_product]

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(brands, avg_discounts, color="orange")
plt.xlabel("Marcas de Producto")
plt.ylabel("Descuento Promedio (%)")
plt.title("Descuento Promedio por Producto")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()


# Consulta para obtener las ventas por fecha
sales_by_date = (
    session.query(Sales.sale_date, func.sum(Sales.final_amount))
    .group_by(Sales.sale_date)
    .all()
)

# Preparar los datos para el gráfico de líneas
dates = [item[0] for item in sales_by_date]
total_sales = [item[1] for item in sales_by_date]

# Crear el gráfico de líneas
plt.figure(figsize=(12, 6))
plt.plot(dates, total_sales, marker="o", linestyle="-", color="purple")
plt.xlabel("Fecha de Venta")
plt.ylabel("Total de Ventas ($)")
plt.title("Ventas por Fecha")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

# Consulta para obtener la distribución de edades de los clientes
from datetime import date

current_year = date.today().year

customers_age = session.query(
    current_year - func.extract("year", Customer.date_birth)
).all()

# Preparar los datos para el gráfico de barras
ages = [item[0] for item in customers_age]

# Crear el gráfico de barras
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=20, edgecolor="black", alpha=0.7)
plt.xlabel("Edad")
plt.ylabel("Cantidad de Clientes")
plt.title("Distribución de Edades de los Clientes")
plt.tight_layout()
plt.show()
