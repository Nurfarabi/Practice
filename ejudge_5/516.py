import re 

s = input()
k = re.search(r"Name: ([A-Za-z' ]+), Age: (\d+)", s)
print(k.group(1), k.group(2))