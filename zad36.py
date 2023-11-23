def factorialRecursive(f):
    if f == 0 or f == 1:
        return 1
    else:
        return f * factorialRecursive(f - 1)


print(f"5!= {str(factorialRecursive(5))}")
