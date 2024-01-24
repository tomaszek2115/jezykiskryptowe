base_number = int(input("podaj podstawe: "))
new_base_number = base_number
iteration_amount = int(input("podaj liczbe iteracji: "))
with open("zad31.txt", 'w') as file:
    file.write("licznik   suma\n")
    file.write("---- ----\n")
    for _ in range(1, iteration_amount+1):
        file.write(f"**{str(_).rjust(1)}**|**{str(new_base_number).ljust(1)}**\n")
        new_base_number += base_number
