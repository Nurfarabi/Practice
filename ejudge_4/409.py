def power2(n):
    for i in range(0, n+1):
        yield 2**i

n = int(input())
for i in power2(n):
    print(i, end=" ")