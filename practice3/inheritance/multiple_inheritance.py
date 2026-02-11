class A:
    pass

class B:
    pass

class C(A, B):
    pass





class Fly:
    def move(self):
        print("Flying")

class Walk:
    def move(self):
        print("Walking")

class Bird(Fly, Walk):
    pass






class X:
    x = 1

class Y:
    y = 2

class Z(X, Y):
    pass





class One:
    def hello(self):
        print("One")

class Two:
    def hi(self):
        print("Two")
