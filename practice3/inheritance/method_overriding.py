class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")



class Animal:
    def sound(self):
        print("Sound")

class Cat(Animal):
    def sound(self):
        print("Meow")




class Shape:
    def area(self):
        return 0




class Square(Shape):
    def area(self):
        return 4
