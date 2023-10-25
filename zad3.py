import random
triesQuantity=10000000

def monteCarlo(triesQuantity):
    circleSurface = 0
    for i in range(triesQuantity):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2+y**2
        if distance<=1:
            circleSurface+=1
    return(circleSurface/triesQuantity)*4

print (f"Estimated value: ", monteCarlo(triesQuantity))

