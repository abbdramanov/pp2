class Parent:
    def __init__(self):
        print("Parent")

class Child(Parent):
    def __init__(self):
        super().__init__()



class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        super().show()




class Shape:
    def __init__(self, name):
        self.name = name



class Square(Shape):
    def __init__(self):
        super().__init__("Square")
