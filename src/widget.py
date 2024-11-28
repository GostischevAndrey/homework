from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_card: str) -> str:
    """Функция маскировки карты и счета"""
    if "Счет" in number_card:
        return "Счет " + get_mask_account(number_card)
    else:
        cards = get_mask_card_number(number_card[-16:])
        new_card = number_card.replace(number_card[-16:], cards)
        return new_card


def get_data(data: str) -> str:
    """Функиия которая сокращает дату до привычного значения"""
    return f"{data[8:10]}.{data[5:7]}.{data[0:4]}"
