# Inheritance: Allows one class(child) to reuse the properties and methods of another class(parent)


#parent class
class Student:
    def __init__(self,name,grade,percentage,team):
        self.name = name
        self.grade = grade
        self.percentage = percentage
        self.team = team
    
    def student_details(self):
        print(f"{self.name} is in garde {self.grade} with {self.percentage}% from team{self.team}")

Team1 = 'A'
Team2 = 'B'

Student1 = Student('Vivek',11,89,Team1)
Student2 = Student('Aman',12,90,Team2)

#child class 
class GraduateStudent(Student):
    def __init__(self,name,grade,percentage,team,stream):
        #parameters from parent class and new parameters from child class 
        super().__init__(name,grade,percentage,team) #call parent class initializer 
        self.stream = stream #new attribute in child class 

    def student_details(self):
        super().student_details()
        print(f'stream is {self.stream}')

Grad_Student1 = GraduateStudent('Vivek',12,98,'A','PCM')
# print(Grad_Student1.__dict__)

Grad_Student1.student_details()