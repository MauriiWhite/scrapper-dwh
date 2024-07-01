from models.database import Customer, Product, Sales, Branch


def map_to_product(row):
    return Product(
        product_id=row["productID"],
        brand=row["brand"],
        description=row["description"],
        price=row["price"],
        reference=row["reference"],
        discount=row["discount"],
    )


def map_to_branch(row):
    return Branch(
        branch_id=row["branchID"],
        branch_name=row["branchName"],
        city=row["city"],
        email=row["email"],
        phone=row["phone"],
        address=row["address"],
        commune=row["commune"],
        opening_date=row["openingDate"],
        closing_hours=row["closingHours"],
        opening_hours=row["openingHours"],
        total_employees=row["totalEmployees"],
        total_products_in_stock=row["totalProductsInStock"],
    )


def map_to_customer(row):
    return Customer(
        customer_id=row["customerID"],
        first_name=row["firstName"],
        last_name=row["lastName"],
        email=row["email"],
        phone=row["phone"],
        gender=row["gender"],
        date_birth=row["dateBirth"],
        total_purchases=row["totalPurchases"],
        registration_date=row["registrationDate"],
    )


def map_to_sales(row):
    return Sales(
        sale_id=row["saleID"],
        product_id=row["productID"],
        customer_id=row["customerID"],
        branch_id=row["branchID"],
        sale_date=row["saleDate"],
        quantity=row["quantity"],
        discount=row["discount"],
        final_amount=row["finalAmount"],
        total_amount=row["totalAmount"],
    )
