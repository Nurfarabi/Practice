n = int(input())
sdd = {}

for i in range(n):
    s, k= input().split()
    k = int(k)
    if s not in sdd:
        sdd[s] = k
    else:
        sdd[s] += k 

for s in sorted(sdd):
    print(s, sdd[s])
