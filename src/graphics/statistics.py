from typing import List, Tuple, Any

from .plotters import plot_bar, plot_pie, plot_hist
from .operations import (
    total_products_sold,
    revenues_per_branch,
    customers_by_gender,
    avg_discount_per_product,
    sales_by_date,
    customers_age,
)


def extract_axis(items: List[Tuple[Any, Any]]) -> Tuple[List[Any], List[Any]]:
    x = [item[0] for item in items]
    y = [item[1] for item in items]
    return x, y


plot_bar(
    figsize=(10, 6),
    axis=extract_axis(total_products_sold),
    labels=["Marcas de Producto", "Cantidad Vendida"],
    title="Total de productos vendidos por marca",
)

plot_bar(
    figsize=(10, 6),
    axis=extract_axis(revenues_per_branch),
    labels=["Ingresos", "Sucursal"],
    title="Ingresos por Sucursal",
    is_barh=True,
)

plot_pie(
    axis=extract_axis(customers_by_gender),
    figsize=(8, 8),
    title="Distribución de Clientes por Género",
)

plot_bar(
    axis=extract_axis(avg_discount_per_product),
    labels=["Marcas de Producto", "Descuento Promedio (%)"],
    figsize=(10, 6),
    title="Descuento Promedio por Producto",
)

plot_bar(
    figsize=(12, 6),
    axis=extract_axis(sales_by_date),
    labels=["Fecha de Venta", "Total de Ventas ($)"],
    title="Ventas por Fecha",
)

plot_hist(
    figsize=(10, 6),
    content=[item[0] for item in customers_age],
    labels=["Edad", "Cantidad de Clientes"],
    title="Distribución de Edades de los Clientes",
)
