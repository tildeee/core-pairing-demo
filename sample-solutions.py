# Solution

def get_digits(characters):
    number = ""
    for char in characters:
        if char.isnumeric():
            number.append(char)
    return int(number)


# Solution for Bonus Challenge #1


def get_digits(characters):
    dec_place = 1
    final_num = 0

    for i in range(len(characters) - 1, -1, -1):
        if characters[i].isnumeric():
            final_num += int(characters[i]) * dec_place
            dec_place *= 10

    return final_num


# Solution for Bonus Challenge #2


def get_digits(characters):
    dec_place = 1
    final_num = 0

    for i in range(len(characters), 0, -1):
        if ord(characters[i]) >= 48 and ord(characters[i]) <= 57:
            final_num += int(characters[i]) * dec_place
            dec_place *= 10

    return final_num
