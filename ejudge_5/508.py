import re 

s = input()
b = input()
k = re.split(b, s)
print(",".join(k))