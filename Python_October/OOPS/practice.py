''' 1.Define a Python class named Student with attributes: name, grade, percentage, and team.
Include an __init__ method to initialize these attributes.
Add a method student_details that prints the student’s details in the format:
"<name> is in <grade> grade with <percentage>%, from team <team>".

2.Create two teams (team1 and team2) as string variables.
3.Create at least two student objects, each belonging to one of teams
4.Call the student_details method for each student to display their details '''


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



print(Student1.__dict__)
print(Student2.__dict__)

Student1.student_details()
Student2.student_details()