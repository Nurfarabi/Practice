def squares(a, b):
    for i in range(a, b +1):
        yield i*i

n, m = map(int, input().split())
for i in squares(n, m):
    print(i)