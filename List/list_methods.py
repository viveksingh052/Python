#append()
# lst1 = [1,2,3,4]
# lst1.append(5)
# print(lst1)

#extend()
# a = [1,2,3,4]
# b = [5,6]

# a.extend(b)
# print(a)
# print(b)

#insert()
# lst1 = [1,2,3,4,5]
# lst1.insert(1,5)
# print(lst1)

#remove()
# lst2 = [1,2,3,4,5]
# lst2.remove(2)
# print(lst2)

#pop()
# a = [1,2,3,4,5]
# a.pop(1)
# print(a)

#clear()
# lst1 = [1,2,3,4,5]
# lst1.clear()
# print(lst1)

#index()
# lst1 = [1,2,3,4,5]
# a = lst1.index(3)
# print(a)

#count
# lst1 = [1,1,2,3,4,5,1,1,1]
# a = lst1.count(1)
# print(a)

#sort
# lst1 = [5,4,1,6,2,4,3]
# lst1.sort()
# print(lst1)

#reverse
# lst1 = [5,4,3,2,1]
# lst1.reverse()
# print(lst1)

#copy
# lst1 = [1,2,3,4]
# lst2 = lst1.copy()

# lst2[0] = 100
# print(lst1)
# print(lst2)

#min() and max()
# lst1 = [1,2,3,4,5]
# print(min(lst1))

# lst1 = [1,2,3,4,5]
# print(max(lst1))


'''to find the common elements on both the list
first convert the list to set 
then use the intersection method which is available in set
the convert that set into list'''

lst1 = [1,2,3,4,5]
lst2 = [3,4,7,8,9]

a = set(lst1)
b = set(lst2)

c = a.intersection(b)
print(list(c))






