def squares(N):
    for i in range(1, N+1):
        yield i*i

n = int(input())
for i in squares(n):
    print(i)