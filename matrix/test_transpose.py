import pytest
from transpose import transpose


@pytest.mark.parametrize('_input, expected', [
    ([[1]], [[1]]),
    ([[1], [-1]], [[1, -1]]),
    ([[1, 2, 3]], [[1], [2], [3]]),
    ([[1], [2], [3]], [[1, 2, 3]]),
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]),
    ([[0, 0, 0], [1, 1, 1]], [[0, 1], [0, 1], [0, 1]]),
    ([[0, -1, -2, -3], [4, 5, 6, 7], [2, 3, -2, -3], [42, 100, 30, -42]],
     [[0, 4, 2, 42], [-1, 5, 3, 100], [-2, 6, -2, 30], [-3, 7, -3, -42]])
])
def test_transpose(_input, expected):
    _ouput = transpose(_input)
    assert _ouput == expected, (
        f"For matrix {_input}, expected {expected} but got {_ouput}")
