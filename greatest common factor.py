num1 = int(input("give me your first number"))
num2 = int(input("give me your second number"))
def gcf(x, y):
    if x > y:
        num = y
    else:
        num = x
    for i in range(1, num+1):
        if((x % i == 0) and (y % i == 0)):
            word = i
    return word

print("gcf is", gcf(x,y))