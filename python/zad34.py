import os
target_directory = "metki"

os.makedirs(target_directory, exist_ok=True)

genders = ["mezczyzna", "kobieta"]
colors = ["bialy", "czarny", "zielony", "czerwony", "niebieski", "zolty", "szary"]
sizes = ["XXL", "XL", "L", "M", "S", "XS"]

label_iteration = 1

for gender in genders:
    for color in colors:
        for size in sizes:
            file_name = f"{target_directory}/metka{label_iteration}.txt"
            with open(file_name, 'w') as file:
                file.write(gender + " " + color + " " + size)
            label_iteration += 1
