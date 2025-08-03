# Recursion is a functions that calls itself

# 1. Factorial
def factorial(num):
    if num<=1:
        return 1
    return num*factorial(num-1)
print(factorial(5))

# 2. Fibonacci
def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
    
print(fibonacci(10))