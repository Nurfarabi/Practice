# Using __init__ method

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Aida", 20)
print(p.name, p.age)