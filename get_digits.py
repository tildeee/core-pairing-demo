import pytest

def get_digits():
    pass


def test_get_digits():
    input = "0fg3y5!78hw578!"

    assert get_digits(input) == 3578578
