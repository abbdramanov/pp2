nums = [3, 1, 2]
print(sorted(nums, key=lambda x: x))



words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda x: len(x)))



words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda x: len(x)))



names = ["Ali", "aLI", "ali"]
print(sorted(names, key=lambda x: x.lower()))
