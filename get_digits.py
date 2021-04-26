import pytest

def get_digits(input):
    final_num = ""
    for char in input:
        if char.isnumeric():
            final_num += char

    return int(final_num)


def test_get_digits():
    input = "0fg3y5!78hw578!"

    assert get_digits(input) == 3578578
