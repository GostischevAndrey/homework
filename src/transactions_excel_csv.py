from typing import Any, Hashable

import pandas as pd


def read_transactions_excel(file_excel: str) -> list[dict[Hashable, Any]] | None:
    """Функция для чтения финансовых транзакций из Excel-файла"""
    try:
        excel_pd = pd.read_excel(file_excel)
        return excel_pd.to_dict(orient='records')
    except FileNotFoundError:
        excel_pd = None
        return excel_pd


def read_transactions_csv(file_csv: str) -> list[dict[Hashable, Any]] | None:
    """Функция чтения финансовых транзакций из CSV-файла"""
    try:
        csv_pd = pd.read_csv(file_csv, sep=';')
        return csv_pd.to_dict(orient='records')
    except FileNotFoundError:
        csv_pd = None
        return csv_pd


print(read_transactions_excel("../data/transactions_excel.xlsx"))
print(read_transactions_csv("../data/transactions.csv"))
