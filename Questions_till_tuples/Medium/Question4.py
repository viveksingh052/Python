#4.Create a list of numbers and print only the even numbers using a for loop.

lst1 = [i for i in range(1,11)]
print("The original list : ",lst1)


for i in lst1 :
    if i%2==0:
        print(i)