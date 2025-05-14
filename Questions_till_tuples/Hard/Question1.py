#1. Write a Python function that returns the factorial of a given number using recursion

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)




n = int(input("Enter the number : "))
result = factorial(n)
print(result)