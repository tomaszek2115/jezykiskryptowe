import statistics

with open('zad16.txt', 'r') as file:
    line = file.readline().strip()
    numList = [int(num) for num in line.split()]

print("srednia", statistics.mean(numList))
print("suma", sum(numList))
print("mediana", statistics.median(numList))

