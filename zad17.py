def inputInteger():
    while True:
        try:
            num = int(input("podaj liczbe calkowita: "))
            return num
            break
        except ValueError:
            print("zly input")

print(inputInteger())