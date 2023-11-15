num = input("podaj liczbe: ")


with open('wyjsciezadanie.txt', 'w') as file:
    for _ in range(7):
        for _ in range(5):
            file.write(num + " ")
        file.write("\n")