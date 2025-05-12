#list comprehension is a very concise , powerful and readable method to create list

#problem to find the squares from 1 to 10 and stores in an empty using loops
# squares = []

# for i in range(1,11):
#     squares.append(i**2)

# print(squares)

#same we can do with the help of list comprehension 

# [expression for item in iterable if condition]
squares = [i**2 for i in range(1,11) if i%2 == 0]
print(squares)