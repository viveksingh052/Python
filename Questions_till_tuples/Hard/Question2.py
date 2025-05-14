#2. Given a list of integers, write a program to remove duplicates without using set()

lst = [1,2,2,1,3,4,4,3]
lst1 = []

for i in lst:
    if i not in lst1:
        lst1.append(i)

print(lst1)