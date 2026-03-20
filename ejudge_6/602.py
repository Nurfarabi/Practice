n = int(input())
d = list(map(int, input().split()))

even = filter(lambda x: x%2==0, d)

print(len(list(even)))