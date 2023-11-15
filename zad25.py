
with open('danezadanie.txt', 'r') as file:
    num1 = file.readline()

num2 = oct(int(num1))
num3 = hex(int(num1))

with open('liczbykonwertowane.txt', 'w') as file:
    file.write(str(num1) + '\n')
    file.write(str(num2) + '\n')
    file.write(str(num3) + '\n')