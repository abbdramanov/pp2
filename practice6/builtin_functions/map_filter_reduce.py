from functools import reduce

nums = [1, 2, 3, 4, 5]

# map()
squared = list(map(lambda x: x**2, nums))
print("Squared:", squared)

# filter()
even = list(filter(lambda x: x % 2 == 0, nums))
print("Even numbers:", even)

# reduce()
sum_all = reduce(lambda x, y: x + y, nums)
print("Sum:", sum_all)