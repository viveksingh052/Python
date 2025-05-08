name = "vivek SINGH" #lower
print(name.lower())

full_name = "vivek singh" #upper
print(name.upper())

text = "python programming" #capitalize
print(text.capitalize())

text1 = "python is the programming language" #title
print(text1.title())

text2 = "abCD" #swapcase
print(text2.swapcase())

text3 = "Python is the programming language" #find
print(text3.find("P"))
print(text3.find("p"))

text4 = "Python programming"  #replace
print(text4.replace("Python","Java"))

text5 = "a,b,c" #split
print(text5.split(','))
s = text5.split(',') 

result = ",".join(s) #join
print(result)

text6 = "python programming"
print(text6.startswith("py")) #startswith
print(text6.endswith("ng")) #endswith

text7 = "vivek1" #isalpha
print(text7.isalpha())

text8 = "123" #isdigit
print(text8.isdigit())

text9 = "125vivek" #isalnum
print(text9.isalnum())



