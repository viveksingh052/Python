#9. Explain the difference between append() and extend() in lists with examples.

# lst1 = [1,2,3,4,5]

# #if we want to add an element to a list we use append() method 

# lst1.append(6)
# print(lst1)


# #if we want to add number of elements in a list we can use extend method

# lst2  = [7,8,9,10]
# lst1.extend(lst2)
# print(lst1)


lst3 = [1,2,3]
lst3.append([4,5])
print(lst3)


lst4 = [1,2,3]
lst4.extend([4,5])
print(lst4)