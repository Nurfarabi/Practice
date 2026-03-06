import re 

s = input()
k = re.findall(r"\b[a-z]{3}\b", s)
print(len(k))