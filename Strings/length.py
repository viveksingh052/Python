text = "python is the king"
print(f"The value of the count using in-built len function is {len(text)}")

#with the help of loops

count = 0  

for i in text:
    count +=1

print(f"The value of the count using for loop is : {count}")

text1 = "python is the king"
i=0
count = 0
while i <len(text1):
    count+=1
    i+=1
print(f"The value of count using while loop is: {count}")