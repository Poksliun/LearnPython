def make_sandwich():
    return ""

def bread_decorator(func):
    def wrapper():
        result = func()
        return "Bread\n" + result + "Bread"
    return wrapper

def salat_decorator(func):
    def wrapper():
        result = func()
        return "Salat\n" + result
    return wrapper

def tomato_decorator(func):
    def wrapper():
        result = func()
        return "Tomato\n" + result
    return wrapper

def meat_decorator(func):
    def wrapper():
        result = func()
        return "Meat\n" + result
    return wrapper

@bread_decorator
@salat_decorator
@tomato_decorator
@meat_decorator
def make_sandwich():
    return ""

print(make_sandwich())