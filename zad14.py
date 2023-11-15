while True:
    try:
        num = int(input("podaj liczbe calkowita: "))
        break
    except ValueError:
        print("zly input")
print(f"prawidlowo: {num}")