import pytest

from app.calculator import calculate_average


def test_calculate_average():
    assert calculate_average([90, 80, 100]) == 90


def test_calculate_average_same_values():
    assert calculate_average([5, 5, 5]) == 5


def test_calculate_average_empty():
    with pytest.raises(ValueError):
        calculate_average([])
