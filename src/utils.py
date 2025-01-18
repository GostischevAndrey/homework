import json
import logging
import os
from typing import Any, Dict, List

from src.external_api import get_amount

logging.basicConfig(
    filename='../logs/utils.log',
    level=logging.INFO,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filemode="w",
    encoding='utf-8'
)
transactions_from_json_logger = logging.getLogger()
transaction_amount_logger = logging.getLogger()


def load_transactions_from_json(file_path: str) -> List[Dict]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    if not os.path.isfile(file_path):
        transactions_from_json_logger.error("Файл транзакций не найден")
        return []

    transactions_from_json_logger.info("Открываем файл транзакций")
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            transactions_from_json_logger.error("Ошибка файла транзакций")
            return []

    if not isinstance(data, list):
        transactions_from_json_logger.error("Список транзакций пуст")
        return []
    else:
        transactions_from_json_logger.info("Создан список словарей с данными о финансовых транзакциях")
        return data


def transaction_amount(trans: dict, currency: str = "RUB") -> Any:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях"""
    if trans["operationAmount"]["currency"]["code"] == currency:
        amount = trans["operationAmount"]["amount"]
        transaction_amount_logger.info("Код валюты в транзакции RUB")
    else:
        amount = get_amount(trans)
        transaction_amount_logger.info("Код валюты транзакции не RUB, делаем конвертацию")
    return amount
