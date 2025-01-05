import json
import os
from typing import Any, Dict, List

from src.external_api import get_amount


def load_transactions_from_json(file_path: str) -> List[Dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    if not os.path.isfile(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            return []

    if isinstance(data, list):
        return data
    else:
        return []


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
    else:
        amount = get_amount(trans)
    return amount


# if __name__ == "__main__":
#     transactions = load_transactions_from_json('../data/operations.json')
#     print(transactions)
