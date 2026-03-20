n = int(input())
d = list(map(int, input().split()))

suma = map(lambda x: x*x, d)

print(sum(suma))