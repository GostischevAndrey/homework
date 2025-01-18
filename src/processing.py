def filter_by_state(list_of_elem: list, state: str = "EXECUTED") -> list:
    """Функция, возвращающая список только тех словарей,
    где ключу 'state' соответствуют аргументу state"""
    state_exec_list_elem = []
    for elem in list_of_elem:
        if elem.get("state") == state:
            state_exec_list_elem.append(elem)
        if "state" not in elem:
            return list_of_elem
    return state_exec_list_elem


def sort_by_date(inform_state: list, reverse: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки."""
    return sorted(inform_state, key=lambda new_operations: new_operations["date"], reverse=reverse)
