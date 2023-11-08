arr1 = []
bool = True
int = 1
string = "word"
arr1.append(bool)
arr1.append(string)
arr1.append(int)

arr2=[]
bool=True
arr2.append(7)
arr2.append("7")
arr2.append(bool)

if len(arr1) != len(arr2):
    print("inna dlugosc")
else:
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            print("inny element")
            break
        else:
            print("listy te same")