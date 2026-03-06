import re  

s = input()
k = re.findall("[A-Z]", s)
print(len(k))