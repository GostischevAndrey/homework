import logging

logging.basicConfig(
    filename='../logs/masks.log',
    level=logging.INFO,
    format="%(levelname)s: %(filename)s: %(funcName)s %(lineno)s: %(asctime)s - %(message)s",
    filemode="w",
    encoding='utf-8'
)
mask_card_logger = logging.getLogger()
mask_account_logger = logging.getLogger()


def get_mask_card_number(card_number: str) -> str:
    """Функция для маскировки номера карты"""
    mask_card_logger.info("Создаем маску номера карты")
    if len(card_number) == 16 and card_number.isdigit():
        mask_card_logger.info("Маска карты успешно создана")
        return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
    mask_card_logger.error("Введен некорректный номер карты")
    return "Некорректный ввод"


def get_mask_account(account_number: str) -> str:
    """Функция для маскировки номера счета"""
    mask_account_logger.info("Создаем маску номера карты")
    if len(account_number) == 20 and account_number.isdigit():
        mask_account_logger.info("Маска счета успешно создана")
        return f"**{account_number[-4:]}"
    mask_card_logger.error("Введен некорректный номер счета")
    return "Некорректный ввод"

# Для проверки функций
# print(get_mask_card_number("Maestro 1596837868705199"))
# print(get_mask_account("Счет 64686473678894779589"))
# print(get_mask_card_number("MasterCard 7158300734726758"))
# print(get_mask_account("Счет 35383033474447895560"))
# print(get_mask_card_number("6831982476737658"))
# print(get_mask_card_number("8990922113665229"))
# print(get_mask_card_number("5999414228426353"))
# print(get_mask_card_number("6831982476737658"))
# print(get_mask_account("35383033474447895560"))
# print(get_mask_account("64686473678894779589"))
