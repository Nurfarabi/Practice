import re

s = input()
n = input()
k = input()

f = re.sub(n, k, s)
print(f)