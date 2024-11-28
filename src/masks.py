def get_mask_card_number(card_number: str) -> str:
    """Функция формирует замаскированный номер карты"""
    card_number = str(card_number)  # Преобразуем в строку введенные данные
    masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    return masked_number


def get_mask_account(mask_account: str) -> str:
    """Функция формирует замаскированный номер счета"""
    mask_account = str(mask_account)  # Преобразуем в строку введенные данные
    masked_account = f"**{mask_account[-4:]}"
    return masked_account
