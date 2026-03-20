fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 95]

for name, score in zip(names, scores):
    print(name, score)

pairs = list(zip(names, scores))
print(pairs) # [('Alice', 85), ('Bob', 90), ('Charlie', 95)]

for i, (name, score) in enumerate(zip(names, scores), start=1):
    print(i, name, score)