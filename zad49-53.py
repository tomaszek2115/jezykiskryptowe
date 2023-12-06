import math


class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        result_real = self.real + other.real
        result_imaginary = self.imaginary + other.imaginary
        return Complex(result_real, result_imaginary)

    def __mul__(self, other):
        result_real = self.real * other.real - self.imaginary * other.imaginary
        result_imaginary = self.real * other.imaginary + self.imaginary * other.real
        return Complex(result_real, result_imaginary)

    def __truediv__(self, other):
        buffered_complex = Complex(other.real, -other.imaginary)
        numerator = self * buffered_complex
        denominator = other * buffered_complex
        result = f"{numerator} / {denominator}"
        return result

    def module(self):
        result = math.sqrt(self.real**2 + self.imaginary**2)
        return result

    def __str__(self):
        return "{} + {}i".format(self.real, self.imaginary)


complex1 = Complex(2, 3)
complex2 = Complex(1, 9)

print(f"Sum = {complex1 + complex2}")
print(f"Mul = {complex1 * complex2}")
print(f"Div = {complex1 / complex2}")
print(f"Mod = {complex1.module()}")
