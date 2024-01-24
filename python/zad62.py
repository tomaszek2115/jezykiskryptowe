class Power:
    def pow(self, x, n):
        return x ** n

calculator = Power()

base = 4
exponent = 2

result = calculator.pow(base, exponent)
print(f"{base}^{exponent}={result}")