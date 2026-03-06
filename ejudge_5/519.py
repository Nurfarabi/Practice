import re 

s = input()
pattern = re.compile("\s")
k = re.findall(pattern, s)
print(len(k)+1)