def convert(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    previous = 0

    for char in reversed(s):
        value = roman[char]

        if value < previous:
            result -= value

        else:
            result += value

        previous = value

    return result

print(convert("MMCXXXVII"))  