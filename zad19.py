import random

l1 = int(input("podaj dolna granice: "))
l2 = int(input("podaj gorna granice: "))

num1 = random.randint(l1, l2)

with open('zad16.txt', 'r') as file:
    line = file.readline().strip()
    numList = [int(num) for num in line.split()]

num2 = random.choice(numList)

with open('wynikzadanie.txt', 'w') as file:
    file.write(str(num1) + " ")
    file.write(str(num2))
