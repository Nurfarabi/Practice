class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return Pair(self.x + other.x, self.y + other.y)
    
x1, y1, x2, y2 = map(int, input().split())
p1 = Pair(x1, y1)
p2 = Pair(x2, y2)

s = p1.add(p2)
print(f"Result: {s.x} {s.y}")