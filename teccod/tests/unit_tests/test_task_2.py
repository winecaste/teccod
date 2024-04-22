import pytest

from teccod.src.task_2 import primes_in_range

@pytest.mark.parametrize("min_num, max_num, expected_output", [
    (1, 10, [2, 3, 5, 7]),
    (10, 20, [11, 13, 17, 19]),
    (20, 30, [23, 29]),
    (30, 40, [31, 37]),
    (40, 50, [41, 43, 47]),
    (50, 60, [53, 59]),
    (1, 2, [2]),
    (10, 11, [11]),
    (20, 21, []),
    (30, 31, [31]),
    (40, 41, [41]),
    (50, 51, []),
    (100, 200, [101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199])
])
def test_primes_in_range(min_num, max_num, expected_output):
    assert primes_in_range(min_num, max_num) == expected_output

