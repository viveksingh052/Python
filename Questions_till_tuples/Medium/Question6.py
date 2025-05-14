#6. Write a program to find the largest of three numbers using if-elif-else.

a = float(input("Enter the first number : "))
b = float(input("Enter the second number : "))
c = float(input("Enter the third number : "))

if a > b and a > c:
    print("a is largest among all the rest numbers.")
elif b > a and b > c:
    print("b is largest among all the rest numbers.")
else:
    print("c is largest")