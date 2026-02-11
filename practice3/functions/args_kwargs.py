def total(*numbers):
    print(sum(numbers))

total(1, 2, 3)



def show(*args):
    for x in args:
        print(x)

show("a", "b", "c")




def info(**data):
    print(data)

info(name="Ali", age=20)



def mix(a, *args, **kwargs):
    print(a, args, kwargs)

mix(1, 2, 3, x=4)
