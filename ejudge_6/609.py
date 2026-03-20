n = int(input())
d = input().split()
c = input().split()
z = input()
data = dict(zip(d, c))
if z in data:
    print(data[z])
else:
    print("Not found")