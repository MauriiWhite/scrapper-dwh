from sqlalchemy import Column, DECIMAL, VARCHAR, INT, TEXT, CHAR, TIME, DATE, ForeignKey
from sqlalchemy.orm import relationship
from database.conection import Base


class Product(Base):
    __tablename__ = "products"

    product_id = Column(INT, primary_key=True)
    brand = Column(VARCHAR(100), nullable=False)
    description = Column(TEXT, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    reference = Column(DECIMAL(10, 2), nullable=False)
    discount = Column(DECIMAL(4, 2), nullable=False)

    sales = relationship(
        "Sales", back_populates="product", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Product(product_id={self.product_id}, brand='{self.brand}')>"


class Customer(Base):
    __tablename__ = "customers"

    customer_id = Column(INT, primary_key=True)
    first_name = Column(VARCHAR(100), nullable=False)
    last_name = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(200), nullable=False)
    phone = Column(VARCHAR(20), nullable=False)
    gender = Column(CHAR(1), nullable=False)
    date_birth = Column(DATE, nullable=False)
    total_purchases = Column(INT, nullable=False)
    registration_date = Column(DATE, nullable=False)

    sales = relationship(
        "Sales", back_populates="customer", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Customer(customer_id={self.customer_id}, email='{self.email}')>"


class Branch(Base):
    __tablename__ = "branches"

    branch_id = Column(INT, primary_key=True)
    branch_name = Column(VARCHAR(200), nullable=False)
    city = Column(VARCHAR(100), nullable=False)
    email = Column(VARCHAR(200), nullable=False)
    phone = Column(VARCHAR(20), nullable=False)
    address = Column(TEXT, nullable=False)
    commune = Column(VARCHAR(100), nullable=False)
    opening_date = Column(DATE, nullable=False)
    closing_hours = Column(TIME, nullable=False)
    opening_hours = Column(TIME, nullable=False)
    total_employees = Column(INT, nullable=False)
    total_products_in_stock = Column(INT, nullable=False)

    sales = relationship("Sales", back_populates="branch", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Branch(branch_id={self.branch_id}, branch_name='{self.branch_name}')>"


class Sales(Base):
    __tablename__ = "sales"

    sale_id = Column(INT, primary_key=True)
    product_id = Column(INT, ForeignKey("products.product_id"), nullable=False)
    customer_id = Column(INT, ForeignKey("customers.customer_id"), nullable=False)
    branch_id = Column(INT, ForeignKey("branches.branch_id"), nullable=False)

    sale_date = Column(DATE, nullable=False)
    quantity = Column(INT, nullable=False)
    discount = Column(DECIMAL(4, 2), nullable=False)
    final_amount = Column(DECIMAL(10, 2), nullable=False)
    total_amount = Column(DECIMAL(10, 2), nullable=False)

    product = relationship("Product", back_populates="sales")
    customer = relationship("Customer", back_populates="sales")
    branch = relationship("Branch", back_populates="sales")

    def __repr__(self):
        return f"<Sales(sale_id={self.sale_id}, sale_date='{self.sale_date}')>"
