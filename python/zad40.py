from zad38 import bubbleSort, insertionSort, quickSort
import time
import random
from datetime import datetime


def generateRandomNumbers(size):
    return [random.randint(-1000, 1000) for _ in range(size)]


function_list = [bubbleSort, insertionSort, quickSort]
numbers = generateRandomNumbers(5000)
function_time = {}
current_datetime = datetime.now()
current_date = current_datetime.date()

for function in function_list:
    start_time = time.time()
    function(numbers)
    end_time = time.time()
    elapsed_time = end_time - start_time
    function_time[function.__name__] = elapsed_time

with open(f"raport_{str(current_date)}.txt", 'w') as file:
    file.write("RAPORT ALGORYTMOW SORTOWANIA\n")
    for function in function_list:
        file.write(f"{function.__name__} --- {function_time[function.__name__]} --- seconds\n")
