class Math:
    def add(self, a, b):
        return a + b

m = Math()
print(m.add(2, 3))




class Counter:
    def __init__(self):
        self.count = 0
    def inc(self):
        self.count += 1



class Greeter:
    def greet(self):
        print("Hello")




class Lamp:
    def turn_on(self):
        print("ON")
