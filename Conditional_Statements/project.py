# users tell which operation to perform on numbers

num1 = float(input("Enter the first value : "))
num2 = float(input("Enter the second value : "))

choice = input("Enter your choice : ")

if(choice == "+"):
    print(f"Addition of numbers is : {num1 + num2}")

elif(choice == "-"):
    print(f"Subtraction of numbers is : {num1 - num2}")

elif(choice == "*"): 
    print(f"Multiplication of numbers is : {num1 * num2}")

elif(choice == "/"):
    print(f"Divison of numbers is : {num1 / num2}")

elif(choice == "//"):
    print(f"FloorDivison of numbers is : {num1 // num2}")

elif(choice == "**"):
    print(f"Exponential of numbers is : {num1 ** num2}")

else:
    print("Invalid Choice. ")

 