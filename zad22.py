import random

k = int(input("podaj liczbe kolumn: "))
w = int(input("podaj liczbe wierszy: "))

with open('danewygenerowane.txt', 'w') as file:
    for _ in range(w):
        for _ in range(k):
            num = random.randint(1, 9)
            file.write(str(num) + " ")
        file.write("\n")
