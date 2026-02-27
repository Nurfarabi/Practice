def num(N):
    for i in range(N, -1, -1):
        yield i

n = int(input())
for i in num(n):
    print(i)