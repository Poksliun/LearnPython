


def bread(func):
    def wrapper(*args, **kwargs):
        burger ='bread\n'+ func(*args, **kwargs)
        return burger
    return wrapper

def salat(func):
    def wrapper(*args, **kwargs):
        burger = 'salat\n' + func(*args, **kwargs)
        return burger

    return wrapper

def tomato(func):
    def wrapper(*args, **kwargs):
        burger = 'tomato\n' + func(*args, **kwargs)
        return burger

    return wrapper

def meat(func):
    def wrapper(*args, **kwargs):
        burger = 'meat\n' + func(*args, **kwargs)
        return burger

    return wrapper

@bread
@salat
@tomato
@meat
@bread
def make_sandwich():
    return ''

def main():
    print(make_sandwich())

if __name__ == '__main__':
    main()