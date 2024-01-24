import math

# (a)

alfa = 30
beta = 60
print(math.sin(alfa)+math.sin(beta))

# (b)

x = 3
n = 4
print((1 + x)**n)

# (c)

a = 1
b = 8
c = 2
x1 = (-b + math.sqrt(b ** 2 - 4 * a * c) / 2 * a)
x2 = (-b - math.sqrt(b ** 2 - 4 * a * c) / 2 * a)
print(x1, x2)

# (d)


def eToTheX(num):
    return math.e ** num


X = 6
positive_infinity = float('inf')
print(X > eToTheX(X))
print(positive_infinity > X)
