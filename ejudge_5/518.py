import re 

s = input()
k = input()
pattern = re.escape(k)
l = re.findall(pattern, s)
print(len(l))