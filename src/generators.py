from typing import Generator, Iterator, Union


def filter_by_currency(my_list: list[dict], currency_code: str = "USD") -> Union[Iterator[dict], str]:
    """
    Функция, которая принимает на вход список словарей.
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной (например, USD)
    """
    if not my_list:
        return "Список транзакций пуст"
    if currency_code not in ["USD"]:
        return "Код валюты не найден."

    for transaction in my_list:
        if transaction["operationAmount"]["currency"]["code"] == currency_code:
            yield transaction
    return iter([])


def transaction_descriptions(my_list: list[dict]) -> Union[Iterator[dict], str]:
    """
    Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    result = (i.get("description") for i in my_list)
    for x in result:
        yield x
    return iter([])


def card_number_generator(start: int, stop: int) -> Generator[str]:
    """
    Функция для генерирования номера карта в диапазоне
    от 0000 0000 0000 0001
    до 9999 9999 9999 9999
    """
    for number in range(start, stop + 1):
        card_number = str(number)
        while len(card_number) < 16:
            card_number = "0" + card_number
        formated_card_number = f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"

        yield formated_card_number
