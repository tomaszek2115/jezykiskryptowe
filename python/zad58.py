def convert(num):
    arabian = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    roman = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]

    result = ''
    j = 0

    while num > 0:
        for i in range(num // arabian[j]):
            result += roman[j]
            num -= arabian[j]

        j += 1
        
    return result

print(convert(2137))

