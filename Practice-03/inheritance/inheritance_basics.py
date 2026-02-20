# Basic inheritance

class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass

dog = Dog()
dog.sound()