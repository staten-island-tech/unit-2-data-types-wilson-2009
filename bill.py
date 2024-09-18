bill = input("what was the bill")
tip = input("was the service bad, okay, good, or great")
if tip == ("bad"):
    print (f"your bill is {bill * 1}")
elif tip == ("okay"):
    print (f"your bill is {bill * 1.15}")
elif tip == ("good"):
    print (f"your bill is {bill * 1.2}")
elif tip == ("great"):
    print (f"your bill is {bill * 1.25}")