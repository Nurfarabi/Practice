import re 

s = input()
k = re.findall(r"\d{2}.\d{2}.\d{4}", s)
print(len(k))