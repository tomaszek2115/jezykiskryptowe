def whichType():
    user_input = input("podaj liczbe: ")
    try:
       a = int(user_input)
       return type(a)
    except ValueError:
        try:
           a = float(user_input)
           return type(a)
        except ValueError:
           print("blad")

print(whichType())