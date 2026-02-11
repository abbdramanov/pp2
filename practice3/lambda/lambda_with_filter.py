nums = [1, 2, 3, 4]
print(list(filter(lambda x: x % 2 == 0, nums)))



nums = [5, 12, 7]
print(list(filter(lambda x: x > 10, nums)))



words = ["hi", "hello"]
print(list(filter(lambda x: len(x) > 2, words)))



nums = [-1, 2, -3]
print(list(filter(lambda x: x > 0, nums)))
