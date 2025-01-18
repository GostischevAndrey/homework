from typing import Any

import pandas as pd


def read_transactions_excel(file_excel: str) -> list[dict[Any, Any]]:
    """Функция для чтения финансовых транзакций из Excel-файла"""
    try:
        excel_pd = pd.read_excel(file_excel)
        return excel_pd.to_dict(orient='records')
    except FileNotFoundError:
        return []


def read_transactions_csv(file_csv: str) -> list[dict[Any, Any]]:
    """Функция чтения финансовых транзакций из CSV-файла"""
    try:
        csv_pd = pd.read_csv(file_csv, sep=';')
        return csv_pd.to_dict(orient='records')
    except FileNotFoundError:
        return []
