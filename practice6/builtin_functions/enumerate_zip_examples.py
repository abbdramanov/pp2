names = ["Ali", "Aruzhan", "Dias"]
scores = [85, 90, 78]


for index, name in enumerate(names):
    print(index, name)


for name, score in zip(names, scores):
    print(f"{name} scored {score}")


x = "123"
print(type(x))

y = int(x)
print(type(y))