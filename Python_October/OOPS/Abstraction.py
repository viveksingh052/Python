# Abstraction : hiding unecessary details from users through method and class

class Student:
    def __init__(self,name,grade,percentage): # method
        self.name = name #attributes
        self.grade = grade #attributes
        self.percentage = percentage

    def student_details(self):
        print(f"{self.name} is in class {self.grade}, with {self.percentage+2}%")  #hidden from user


# object: Instance of class 
Student_1 = Student('Vivek',12,92)
Student_2 = Student('Aman',11,94)

Student_1.student_details()
Student_2.student_details()

print(Student_1.__dict__)
print(Student_2.__dict__)