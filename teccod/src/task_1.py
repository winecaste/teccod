def unique_elements(lst: list[int]) -> list[int]:
    """
    Функция принимает список целых чисел и возвращает новый список,
    содержащий только уникальные элементы из исходного списка.
    """
    new_lst = []

    for item in lst:
        if item not in new_lst:
            new_lst.append(item)

    return new_lst

