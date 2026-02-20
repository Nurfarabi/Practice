class circle:
    def __init__(self, rad):
        self.rad = rad

    def area(self):
        pi = 3.14159
        return (self.rad**2)*pi
    
r = int(input())
ar = circle(r)
print(f"{ar.area():.2f}")