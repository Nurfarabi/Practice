n = int(input())
sdd = {}

for i in range(1, n+1):
    s = input()
    if s not in sdd:
        sdd[s] = i

for s in sorted(sdd):
    print(s, sdd[s])
