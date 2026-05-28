import json
import os

def cache(filename):
    storage = {}

    def decorator(func):
        def wrapper():
            key = "sandwich"

            if key in storage:
                return storage[key]

            result = func()
            storage[key] = result

            with open(filename, 'w') as f:
                json.dump(storage, f)

            return result
        return wrapper
    return decorator

@cache('sandwich_cache.json')
def make_sandwich():
    return ""

print(make_sandwich())