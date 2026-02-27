def even(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
for i in even(n):
    if i != 0:
        print(",", end="")
    print(i, end="")