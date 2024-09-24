num1 = int(input("give me your first number"))
num2 = int(input("give me your second number"))

print(num1)
print(num2)

for i in range(1, num1 + 1):
    if num1 % i == 0:
        print(i)

for i in range(1, num2 + 1):
    if num2 % i == 0:
        print(i)

if num1 % num2 == 0