import re
 
s = input()

k = re.match("^[A-Za-z].*[0-9]$", s)
if k:
    print("Yes")
else:
    print("No")