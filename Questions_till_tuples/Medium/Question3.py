# 3. Write a program to check whether a given number is even or odd using a function.

def check(n):
    if n%2==0:
        return "It is an even number"
    else:
        return "It is an odd number"
    
        
n= int(input("Enter the value : "))
result = check(n)
print(result)