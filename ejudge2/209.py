n = int(input())

arr = list(map(int, input().split()))

mina = min(arr)
maxa = max(arr)

for i in range(n):
    if arr[i] == maxa:
        arr[i] = mina
    
print(*arr)