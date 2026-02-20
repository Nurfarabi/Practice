n = int(input())
nums = list(map(int, input().split()))

q = int(input())

for _ in range(q):
    parts = input().split()
    op = parts[0]

    if op == "add":
        x = int(parts[1])
        nums = list(map(lambda a: x+a, nums))
    elif op == "multiply":
        x = int(parts[1])
        nums = list(map(lambda a: x*a, nums))
    elif op == "power":
        x = int(parts[1])
        nums = list(map(lambda a: a**x, nums))
    elif op == "abs":
        nums = list(map(lambda a: abs(a), nums))

print(*nums)