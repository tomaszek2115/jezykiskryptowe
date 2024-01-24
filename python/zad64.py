def count(text):
    vowels = "aoeiuyąęAOEIUYĄĘ"
    counter = sum(1 for char in text if char in vowels)
    return counter

text = "kocham języki skryptowe mój ulubiony przedmiot"
print(f"Ilość samogłosek: {count(text)}")