import functools

def retry(count: int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = count
            while attempts > 0:
                try:
                    return func(*args, **kwargs)
                except ValueError:
                    attempts -= 1
                    if attempts == 0:
                        raise
                except OSError:
                    print(f"{func.__name__} raise OsError exception.")
                    attempts -= 1
                    if attempts == 0:
                        raise
            return None
        return wrapper
    return decorator