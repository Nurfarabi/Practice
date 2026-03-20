n = int(input())
d = list(map(str, input().split()))

for i, name in enumerate(d):
    print(f"{i}:{name}", end=" ")