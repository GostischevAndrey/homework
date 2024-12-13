def filter_by_state(list_of_dict: list, state: str = 'EXECUTED') -> list:
    """Функция, возвращающая список только тех словарей,
       где ключу 'state' соответствуют аргументу state"""
    state_exec_list_dicts = []
    for dict in list_of_dict:
        if dict.get("state") == state:
            state_exec_list_dicts.append(dict)
        if "state" not in dict:
            return list_of_dict
    return state_exec_list_dicts


def sort_by_date(inform_state: list, reverse: bool = True) -> list:
    """Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание)."""
    sorted_inform_state = sorted(inform_state, key=lambda inform_state: inform_state.get("date"), reverse=reverse)
    return sorted_inform_state
