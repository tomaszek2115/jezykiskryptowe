def LCG(m,a,c,n):
    x = 1
    result = []

    for i in range(n):
        x=(a*x+c)%m
        result.append(x)
    return result

print(LCG(10,3,4,3))
