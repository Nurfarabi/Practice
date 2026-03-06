import re

s = input()
k = re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+", s)
if k:
    print(k.group())
else:
    print("No email")