a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest is:", a)
elif b >= c:
    print("Greatest is:", b)
else:
    print("Greatest is:", c)
