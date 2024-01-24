from fractions import Fraction

def convert(decimal):
    fraction = Fraction(decimal).limit_denominator()
    return fraction

decimal_number = 0.25
result_fraction = convert(decimal_number)

print(result_fraction)
