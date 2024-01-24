arr = []
print("zacznij wpisywac, aby przerwac pozostaw puste pole i wcisnij enter:\n")
userInput = "a"
while userInput != "":
    userInput = input()
    arr.append(userInput)
for i in range(len(arr)):
    print(arr[i])