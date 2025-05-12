#aliasing
# lst_1 = [1,2,3,4]
# lst_2 = lst_1

# lst_2[0] = 100

# print(lst_1,lst_2)

#then we are using the copy method
lst_1 = [1,2,3,4]
lst_2 = lst_1.copy()

lst_2[0] = 100
print(lst_1,lst_2)


text = "python is the high-level programming language."
print(text.find("python"))