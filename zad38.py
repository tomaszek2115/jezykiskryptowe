# read from file

with open("doposortowania.txt", 'r') as mixed_file:
    line = mixed_file.readline()
    numbers = [int(num) for num in line.split()]

# bubblesort


def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# insertion sort


def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# quicksort


def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quickSort(left) + middle + quickSort(right)


numbers = quickSort(numbers)
with open("posortowane.txt", 'w') as sorted_file:
    for number in numbers:
        sorted_file.write(str(number) + " ")
