userInput = input("Podaj ciąg liter: ")

vowelArr = ["a", "e", "y", "u", "i", "o"]

# Initialize a dictionary to store counts for each vowel
vowel_counts = {vowel: 0 for vowel in vowelArr}

for letter in userInput:
    if letter in vowel_counts:
        vowel_counts[letter] += 1

for vowel, count in vowel_counts.items():
    if count > 0:
        print(f"{vowel} : {count}")
