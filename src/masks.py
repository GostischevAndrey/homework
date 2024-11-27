card_number = int(input())
accound_number = int(input())


def get_mask_card_number(number_card: int) -> str:
    """
    Принимает на вход номер карты и возвращает ее маску.
    """
    str_number_card = str(number_card)
    return f"{str_number_card[0:4]} {str_number_card[4:6]}** **** {str_number_card[-4:]}"


print(get_mask_card_number(card_number))


def get_mask_account(number_account: int) -> str:
    """
    Принимает на вход номер счета и возвращает его маску.
    """
    str_number_account = str(number_account)
    return f"**{str_number_account[-4:]}"


print(get_mask_account(accound_number))
