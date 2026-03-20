s = input().lower()
if any(x in "aeiou" for x in s):
    print("Yes")
else:
    print("No")