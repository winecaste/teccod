def sort_strings_by_length(strings: list[str]) -> tuple[list[str], list[str]]:
    """
    Функция принимает список строк и возвращает два списка:
    1. Список строк, отсортированный по возрастанию длины.
    2. Список строк, отсортированный по убыванию длины.
    """
    sorted_ascending = sorted(strings, key=len)

    sorted_descending = sorted(strings, key=len, reverse=True)

    return sorted_ascending, sorted_descending


