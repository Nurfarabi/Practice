import re 

s = input()
k = re.compile("^\d+$")
l = k.findall(s)
if l:
    print("Match")
else:
    print("No match")