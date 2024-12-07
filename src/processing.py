def filter_by_state(inform_state: list, state: str = "EXECUTED") -> list:
    """Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED')"""
    list_state = []

    for key in inform_state:
        if key.get("state") == state:
            list_state.append(key)
    return list_state


def sort_by_date(inform_state: list, reverse: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)."""
    sorted_inform_state = sorted(inform_state, key=lambda inform_state: inform_state.get("date"), reverse=reverse)
    return sorted_inform_state
