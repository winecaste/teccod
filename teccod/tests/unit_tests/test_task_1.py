import pytest

from teccod.src.task_1 import unique_elements


@pytest.mark.parametrize("input_list, expected_output", [
    ([], []),
    ([5], [5]),
    ([1, 2, 3, 2, 1, 4, 5, 4], [1, 2, 3, 4, 5]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
])
def test_unique_elements(input_list, expected_output):
    assert unique_elements(input_list) == expected_output


