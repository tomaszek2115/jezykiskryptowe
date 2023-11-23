import cmath

with open("wspolczynniki.txt", 'r') as file:
    line = file.readline()
    numbers_str = line.split()
    a, b, c = map(int, numbers_str)

delta = b ** 2 - 4 * a * c
if delta < 0:
    delta_root = cmath.sqrt(delta)
    x1 = (-b - delta_root) / 2*a
    x2 = (-b + delta_root) / 2*a
    print(f"x1: {str(x1)}\nx2: {str(x2)}")
else:
    print("rownanie nie jest w ciele liczb zespolonych")
