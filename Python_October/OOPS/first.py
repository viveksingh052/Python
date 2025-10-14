# OOPS
# class: Blueprint or Template
class Student:
    def __init__(self,name,grade,percentage): # method
        self.name = name #attributes
        self.grade = grade #attributes
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage}%") 


# object: Instance of class 
# Student_1 = Student('Vivek',12,99)
Student_2 = Student('Aman',11,98)

#modify 
# Student_1.percentage = 100
# print(Student_1.percentage)

#delete attribute
# print(Student_1.__dict__)
# del Student_1.percentage
# print(Student_1.__dict__)

#delete object
# del Student_1
# print(Student_1)

