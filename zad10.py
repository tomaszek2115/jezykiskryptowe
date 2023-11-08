arr1 = []
arr1.append(1)
arr1.append(2)
arr1.append(1)
arr1.append(1)
q = 0
for i in range(len(arr1)):
    if arr1[i] == 1:
        q+=1
if q == 0:
    print("nie wystepuje")
else:
    print(f"wystepuje {q} razy")