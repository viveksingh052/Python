#8. Implement a simple calculator using if-elif-else that can perform +, -, *, and / operations.

operation = input("Enter the operator : ")

a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))


if operation == "+":
    print(a+b)
elif operation == "-":
    print(a-b)
elif operation == "*":
    print(a*b)
elif operation == "/":
    print(a/b)
elif operation == "//":
    print(a//b)
elif operation == "%":
    print(a%b)
elif operation == "**":
    print(a**b)
else:
    print("Invalid Operator")