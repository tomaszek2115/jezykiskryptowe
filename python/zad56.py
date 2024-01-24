import random

def shuffleList(list):
    shuffled = list.copy() 
    random.shuffle(shuffled)
    return shuffled

list = [1, 2, 3, 4, 5]

result = shuffleList(list)
print("Oryginalna lista:", list)
print("Wymieszana lista:", result)
