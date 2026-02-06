import math
n = int(input())
s = False
for i in range(2, int(math.sqrt(n))+1):
    if n%i == 0:
        s = True
        break

if s:
    print("No") 
else:
    print("Yes")