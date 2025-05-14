#3. Write a Python program that takes a sentence and prints each word on a new line, sorted alphabetically

sentence = input("Enter the sentence : ").lower()
sen = sentence.split(" ")

print(sen)

sen.sort()
print(sen)
