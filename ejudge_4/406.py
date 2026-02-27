def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, b+a
        

n = int(input())
for i in fibonacci(n):
    if i != 0:
        print(",", end="")
    print(i, end="")