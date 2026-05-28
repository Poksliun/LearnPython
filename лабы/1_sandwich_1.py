def make_sandwich():
    pass

def bread_decorator(func):
    def wrapper():
        print("Bread")
        func()
        print("Bread")
    return wrapper

def salat_decorator(func):
    def wrapper():
        print("Salat")
        func()
    return wrapper

def tomato_decorator(func):
    def wrapper():
        print("Tomato")
        func()
    return wrapper

def meat_decorator(func):
    def wrapper():
        print("Meat")
        func()
    return wrapper

@bread_decorator
@salat_decorator
@tomato_decorator
@meat_decorator
def make_sandwich():
    pass

make_sandwich()