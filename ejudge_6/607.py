n = int(input())
d = list(map(str, input().split()))

print(max(d, key=len))