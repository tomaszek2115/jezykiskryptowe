def getFactorial(f):
    n = 1
    for i in range(1, f+1):
        n *= i
    return n


print(str(getFactorial(5)))
