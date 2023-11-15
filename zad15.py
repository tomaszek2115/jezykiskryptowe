import statistics

def inputInteger():
    while True:
        try:
            num = int(input())
            return num
            break
        except ValueError:
            print("zly input")

numList = []
print("podaj ilosc liczb: ")
q = inputInteger()
print("wpisuj liczby: ")
for _ in range(q):
    numList.append(inputInteger())
print("srednia", statistics.mean(numList))
print("suma", sum(numList))
print("mediana", statistics.median(numList))

