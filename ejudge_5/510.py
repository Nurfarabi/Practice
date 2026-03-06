import re 

s = input()
k = re.search("dog|cat", s)
if k:
    print('Yes')
else:
    print("No")