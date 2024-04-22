def primes_in_range(min_num: int, max_num: int) -> list[int]:
    """
    Функция принимает два целых числа (минимум и максимум) и возвращает список
    всех простых чисел в заданном диапазоне.
    """
    primes = []
    for num in range(min_num, max_num + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes


