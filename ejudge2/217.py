n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

ans = 0
for x in set(arr):
    if arr.count(x) == 3:
        ans += 1
print(ans)
