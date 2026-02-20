def valid(a):
    for i in range(len(a)):
        if int(a[i])%2==1:
            return "Not valid" 
    return "Valid"

a = input()

print(valid(a))