def bread(func):
    def wrapper():
        return f"Bread\n{func()}\nBread"
    return wrapper

def salat(func):
    def wrapper():
        return f"Salat\n{func()}"
    return wrapper

def tomato(func):
    def wrapper():
        return f"Tomato\n{func()}"
    return wrapper

def meat(func):
    def wrapper():
        return f"Meat\n{func()}"
    return wrapper

@bread
@salat
@tomato
@meat
def make_sandwich():
    return ''

def main():
    result = make_sandwich()
    print(result)

if __name__ == '__main__':
    main()