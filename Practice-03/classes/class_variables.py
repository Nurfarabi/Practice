# Class variables vs instance variables

class Student:
    school = "AITU"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

s1 = Student("Aida")
s2 = Student("Dana")

print(s1.school)
print(s2.school)