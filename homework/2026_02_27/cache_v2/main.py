import json
import os


if not os.path.exists('cache.json'):
    with open('cache.json', 'w') as f:
        json.dump({}, f)

def cache(type_of_argument : str):
    def decorator(func):
        def wrapper(*args,**kwargs):
            kwargs_items = sorted(tuple(kwargs.items()))
            func_name= func.__name__
            if type_of_argument == "args":
                key = f"{args}, {func_name}"
            elif type_of_argument == "kwargs":
                key = f"{kwargs_items}, {func_name}"
            else:
                key = f"{args}, {kwargs_items}, {func_name}"
            try:
                with open('cache.json', 'r') as f:
                    cache_json = json.load(f)
            except:
                cache_json={}
            if key in cache_json:
                print("кэш")
                return  cache_json[key]
            func_result =  func(*args,**kwargs)
            cache_json[key]= func_result
            with open('cache.json', 'w') as f:
                json.dump(cache_json,f)
            return func_result
        return wrapper
    return decorator


