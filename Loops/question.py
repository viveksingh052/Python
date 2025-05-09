# write a program to take the start , stop and step value and also input the value which user wants to skip


a = int(input("Enter the start value : "))
b = int(input("Enter the stop value : "))
c = int(input("Enter the step value : "))
d = int(input("Enter the value which you want to skip : "))


if a<b:
    for i in range (a,b,c):
        if i == d:
            continue
        print(i)
else:
    print("your start value is greater than stop value.")