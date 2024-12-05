from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_data, mask_account_card

print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_mask_card_number("6831982476737658"))
print(get_mask_account("35383033474447895560"))
print(get_mask_account("64686473678894779589"))
print(get_data("2024-03-11T02:26:18.671407"))