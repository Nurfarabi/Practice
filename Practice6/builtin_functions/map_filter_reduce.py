nums = [1, 2, 3, 4]

squared = list(map(lambda x: x**2, nums))
print(squared) # [1, 4, 9, 16] 

nums = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, nums))
print(even) # [2, 4, 6]

from functools import reduce

nums = [1, 2, 3, 4]

total = reduce(lambda x, y: x + y, nums)
print(total) # 10 


nums = [1, 2, 3, 4, 5]

result = reduce(
    lambda x, y: x + y,
    filter(lambda x: x % 2 == 0,
           map(lambda x: x * 2, nums))
)

print(result)