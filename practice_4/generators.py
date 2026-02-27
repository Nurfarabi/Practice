def squares(N):
    for i in range(1, N+1):
        yield i*i

n = int(input())
for i in squares(n):
    print(i)

def squares(a, b):
    for i in range(a, b +1):
        yield i*i

n, m = map(int, input().split())
for i in squares(n, m):
    print(i)

def even(n):
    for i in range(0, n + 1):
        if i%3 == 0 and i%4==0:
            yield i
        

n = int(input())
for i in even(n):
    if i != 0:
        print(" ", end="")
    print(i, end="")