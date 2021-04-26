import pytest


def get_digits(input):
    final_num = 0
    digit_place = 1

    for i in range(len(input) - 1, -1, -1):
        char = input[i]
        if char.isnumeric():
            final_num += int(char) * digit_place
            digit_place *= 10

    return final_num


def test_get_digits():
    input = "0fg3y5!78hw578!"

    assert get_digits(input) == 3578578
