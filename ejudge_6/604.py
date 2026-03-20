n = int(input())
d = list(map(int, input().split()))
c = list(map(int, input().split()))
s = 0
for num, num2 in zip(d, c):
    s += num*num2

print(s)