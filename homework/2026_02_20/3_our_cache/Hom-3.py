def cache(func):
    cached_results = {}
    def wrapper(*args):
        if args in cached_results:
            return cached_results[args]
        result = func(*args)
        cached_results[args] = result
        return result
    return wrapper


@cache
def my_sum(a, b):
    return a + b


if __name__ == '__main__':
    print(my_sum(2, 3))
    print(my_sum(2, 3))
    print(my_sum(5, 7))
    print(my_sum(2, 3))