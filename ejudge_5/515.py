import re 

s = input()
def double(m):
    return m.group()*2
k = re.sub("\d", double, s)
print(k)