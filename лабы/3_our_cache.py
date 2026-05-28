def cache(func):
    storage = {}

    def wrapper(*args):
        if args in storage:
            return storage[args]
        else:
            result = func(*args)
            storage[args] = result
            return result

    return wrapper

def my_sum(a, b):
    return a + b

cached_sum = cache(my_sum)

print(my_sum(2, 3))

print(my_sum(5, 7))