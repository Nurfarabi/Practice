def prime(n):
    for i in range(2, n+1):
        for k in range(2, int(i**0.5)+1):
            if i%k == 0:
                break
        else:
            yield i

n = int(input())
for p in prime(n):
    print(p, end=" ")