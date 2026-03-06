from random import random, choice

from my_decorator import retry

exceptions = (ValueError, OSError)

@retry(count=5)
def random_exception() -> float:
    if (d := random()) > 0.5:
        raise choice(exceptions)
    return d


if __name__ == "__main__":
    for _ in range(100):
        print("result:", random_exception())
