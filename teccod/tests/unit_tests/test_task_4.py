import pytest

from teccod.src.task_4 import sort_strings_by_length

@pytest.mark.parametrize("input_strings, expected_ascending, expected_descending", [
    (["a", "ab", "abc", "abcd"], ["a", "ab", "abc", "abcd"], ["abcd", "abc", "ab", "a"]),
    (["abcd", "abc", "ab", "a"], ["a", "ab", "abc", "abcd"], ["abcd", "abc", "ab", "a"]),
    (["abc", "ab", "abcd", "a"], ["a", "ab", "abc", "abcd"], ["abcd", "abc", "ab", "a"]),
    (["abcd", "abc", "a", "ab"], ["a", "ab", "abc", "abcd"], ["abcd", "abc", "ab", "a"]),
    ([], [], []),
    (["world", "hello"], ["world", "hello"], ["world", "hello"]),
    (["longer", "short"], ["short", "longer"], ["longer", "short"]),
    (["short", "longer"], ["short", "longer"], ["longer", "short"]),
    (["", "", ""], ["", "", ""], ["", "", ""]),
])
def test_sort_strings_by_length(input_strings, expected_ascending, expected_descending):
    ascending, descending = sort_strings_by_length(input_strings)
    assert ascending == expected_ascending
    assert descending == expected_descending

