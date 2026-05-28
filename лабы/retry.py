def retry(func):
    def wrapper(*args, **kwargs):
        while True:
            try:
                return func(*args, **kwargs)
            except ValueError:
                continue
            except OSError:
                print(f"{func.__name__} raise OsError exception.")
                continue
    return wrapper