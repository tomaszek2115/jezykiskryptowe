import math

def calculateSurface(num_sides, side_length):
    area = (num_sides * side_length**2) / (4 * math.tan(math.pi / num_sides))
    return area

sides = int(input("podaj ilosc bokow: "))
length = int(input("podaj dlugosc boku: "))

print(calculateSurface(sides, length))
