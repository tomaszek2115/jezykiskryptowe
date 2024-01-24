file_path = "tekstwejsciowy.txt"


def howManyLetters(letter):
    q = 0
    with open(file_path, 'r') as file:
        while True:
            char = file.read(1)
            if char == letter:
                q += 1
            if not char:
                break
    return q


print(howManyLetters('a'))
