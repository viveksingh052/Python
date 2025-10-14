# Encapsulation: Restrict access to certain attributes or methods to protect data and enforce controlled access


class Student:
    def __init__(self,name,grade,percentage): # method
        self.name = name #attributes
        self.grade = grade #attributes
        self.__percentage = percentage # double underscores limit access 

    def get_percentage(self):
        return self.__percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%")  #hidden from user


# object: Instance of class 
Student_1 = Student('Vivek',12,92)
Student_2 = Student('Aman',11,94)

print(Student_1.get_percentage())
print(Student_2.get_percentage())