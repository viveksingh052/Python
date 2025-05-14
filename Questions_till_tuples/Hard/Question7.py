# 7. Write a program to check if a string is a palindrome.

text = input("Enter the string : ")

reverse = ""

for char in text:
    reverse = char + reverse

if(text == reverse):
    print("It is a palindrome string")
else:
    print("Not a palindrome string")
