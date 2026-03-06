import re

m = input()
n = input()
if re.search(n, m):
    print("Yes")
else:
    print("No")