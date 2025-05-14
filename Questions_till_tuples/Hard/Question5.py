#5. Write a program to reverse a string without using built-in functions.

text = "python"

print(text[::-1])

reverse = ""

for i in text:
    reverse = i + reverse

print(f"The value of reverse is :{reverse} ")