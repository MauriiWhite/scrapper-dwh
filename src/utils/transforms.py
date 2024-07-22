import pandas as pd
from pandas import Series

from .typed import DataTyped

# Date: %Y-%m-%d, Phone: 9[0-9]{8}, UTF-8


def correct_encoding(series: Series) -> Series:
    return series.str.encode("latin1").str.decode("utf-8")


def csv_products(file_path: str) -> DataTyped:
    df = pd.read_csv(file_path, encoding="utf-8")
    return df.iterrows()


def json_branches(file_path: str) -> DataTyped:
    df = pd.read_json(
        file_path, convert_dates=["openingDate"], dtype={"phone": str}, encoding="utf8"
    )
    df["openingDate"] = df["openingDate"].dt.strftime("%Y-%m-%d")
    df["phone"] = df["phone"].str.replace(r"^\+56", "", regex=True)
    return df.iterrows()


def xlsx_customers(file_path: str) -> DataTyped:
    df = pd.read_excel(file_path)
    df["gender"] = df["gender"].replace({"female": "f", "male": "m"})

    # Convertir fechas
    df["dateBirth"] = pd.to_datetime(df["dateBirth"], dayfirst=True).dt.strftime(
        "%Y-%m-%d"
    )
    df["registrationDate"] = pd.to_datetime(
        df["registrationDate"], dayfirst=True
    ).dt.strftime("%Y-%m-%d")

    df["firstName"] = correct_encoding(df["firstName"])
    df["lastName"] = correct_encoding(df["lastName"])
    return df.iterrows()


def xml_sales(file_path: str) -> DataTyped:
    df = pd.read_xml(file_path)
    df["saleDate"] = pd.to_datetime(df["saleDate"], format="%Y-%m-%d")
    df["saleDate"] = df["saleDate"].dt.strftime("%Y-%m-%d")
    return df.iterrows()
