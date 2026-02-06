n = int(input())

arr = list(map(int, input().split()))

max_cnt = 0
ans = arr[0]

for i in range(n):
    cnt = 0
    for j in range(n):
        if arr[j] == arr[i]:
            cnt += 1

    if max_cnt < cnt or (max_cnt==cnt and arr[i] < ans):
        max_cnt = cnt
        ans = arr[i]

print(ans)
        