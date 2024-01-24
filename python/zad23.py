user_input = input("wpisz ciag: ")
inverted_string = user_input[::-1]

if inverted_string == user_input:
    print("jest palindromem")
else:
    print("nie jest palindromem")
