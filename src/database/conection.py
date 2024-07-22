from sqlalchemy import create_engine as con
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase

SQLALCHEMY_DATABASE_URL = "mysql://root:@localhost:3306/store"

engine = con(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()


class Base(DeclarativeBase):
    pass
