#2. Explain the difference between == and is in Python with examples.

# == 

lst1 = [1,2,3,4,5]
user = int(input("Enter the number : "))

for i in lst1 :
    if(i == user):
        print(f"The value of {i} is same as {user} value")
        break
else:
    print("Invalid value")  

#it checks the equality of the value whether the value is same or not

# is

a = 15
b = a

print( a is b)

#it checks whether the two variables are pointing the same object in memory

# in 

fruit = ["mango","banana","apple"]
print("banana" in fruit)

#it checks whether the value is present in sequence datatype.