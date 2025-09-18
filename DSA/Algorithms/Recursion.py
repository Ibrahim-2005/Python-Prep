def factorial(number):
    if number==1:
        return 1
    else:
        return number*factorial(number-1)


number=10
print(factorial(number))