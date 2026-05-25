cache_json = {}


def cache(func):
    def wrapper(*args,**kwargs):
        kwargs_items = sorted(tuple(kwargs.items()))
        func_name= func.__name__
        key = f"{args}, {kwargs_items}, {func_name}"
        if key in cache_json:
            print("r")
            return  cache_json[key]
        func_result =  func(*args,**kwargs)
        cache_json[key]= func_result
        return func_result
    return wrapper


@cache
def my_sum(a, b):
    return a + b






