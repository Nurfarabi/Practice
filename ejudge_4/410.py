def cycle(lst, n):
    for _ in range(n):
        for item in lst:
            yield item

lst = input().split()
n = int(input())
for i in cycle(lst, n):
    print(i, end=" ")
