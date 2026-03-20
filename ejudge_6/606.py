n = int(input())
d = list(map(int, input().split()))

if all(x>=0 for x in d):
    print("Yes")
else:
    print("No")