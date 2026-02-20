class parent:
    def __init__(self, name):
        self.name = name

class student(parent):
    def __init__(self, name, gpa):
        super().__init__(name)
        self.gpa = gpa

    def display(self):
        print(f"Student: {self.name}, GPA: {self.gpa}")

name, gpa = input().split()
stu = student(name, float(gpa))
stu.display()