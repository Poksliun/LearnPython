def retry(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if count<=0:
                return "не пошло"
            try:
                result_func = func(*args, **kwargs)
                return result_func
            except ValueError:
                return retry(count-1)(func)(*args, **kwargs)
            except OSError:
                return str(func.__name__) +  " raise OsError exception."

        return wrapper
    return decorator