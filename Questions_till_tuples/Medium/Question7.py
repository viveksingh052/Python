#7. Write a program to count the number of vowels in a string.

lst = ["a","e","i","o","u"]
text = input("Enter the string : ").lower()

count = 0
for i in lst:
    for j in text:
        if(i ==j):
            count +=1
        
print(count)



    