def valid(a):
    while a%2==0: a = a/2
    while a%3==0: a = a/3
    while a%5==0: a = a/5
    if a == 1.0: return "Yes"
    else: return "No"

a = int(input())

print(valid(a))