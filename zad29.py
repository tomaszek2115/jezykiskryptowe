with open("tekstdostatystyki.txt", 'r') as file:
    text = file.read()
    words = text.replace('\n', ' ').replace('\r', '').split(' ')
    words = [word for word in words if word]
    total_words = len(words)
    unique_words = len(set(words))
    word_occurrences = {word: words.count(word) for word in set(words)}
    print("liczba slow: " + str(total_words))
    print("liczba unikalnych slow: " + str(unique_words))
    print("liczba wystapien kazdego slowa: ")
    for word, occurrences in word_occurrences.items():
        print(word + ": " + str(occurrences))
