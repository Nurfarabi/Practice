n = int(input())
arr = list(map(int, input().split()))

k = max(arr)
p = 0
for i in range(n):
    if arr[i] == k:
        p = i+1
        break
print(p)