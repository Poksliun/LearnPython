# """
# arguments.py
# Здесь мы учим функци
# """
#
#
# def foo():
#     """foo docstring"""
#     pass
#
#
# # print(foo.__doc__)
# # print(type(foo))
# # print(foo)
#
# def factorial(n: int) -> int:
#     """factorial calc
#     >>> factorial(3)
#     6
#     """
#     number = 1
#     for i in range(1, n + 1):
#         number *= i
#     return number
#
#
# # f_ = list(map(factorial, [1, 2, 3, 4, 5]))
# # print(f_)
# # print([factorial(i) for i in range(10)])
#
# def is_odd(n: int) -> bool:
#     """
#     >>> is_odd(5)
#     True
#     >>> is_odd(6)
#     False
#     """
#     return bool(n & 1)
#
#
# fl = filter(is_odd, range(10))
# # print(list(fl))
# # print([i for i in range(10) if is_odd(i)])
#
# from functools import reduce
#
#
# # def my_sum(a: int, b: int) -> int:
# #     return a + b
#
# # res = reduce(my_sum, [1, 2, 3, 4])
# # print(res)
#
# def foo_(a=1, b: int = 2, c=3, d=foo, e=.2, f=None, g=(1,)):
#     if f is None:
#         f = []
#         print(id([]))
#     print(id(f))
#     f.append(a)
#     print(a, b, c, d, e, f, g)
#
# # foo_(1, 2)
# # foo_(a=1, b=2)
# # foo_(1, b=3)
#
# # def check(a = print("Hello check")):
# #     pass
#
#
#
# # foo_(9)
# # foo_(5)
#
# # def foo_with_args(a, b, *args):
# #     print(a, b, args)
# #
# # foo_with_args(1, 1, 3, 3)
#
# # def foo_with_kwargs(a, b, *args, **kwargs):
# #     print(a, b, args, kwargs)
# #
# my_arg = [1, 2]
#
# my_kwarg = {'a': 1, "b":2}
# #
# #
# # foo_with_kwargs(*my_arg, **my_kwarg)
# #
#
# def my_func():
#     print("my_func")
#
# my_arg = []
# my_kwarg = {}
#
# my_func(*my_arg, **my_kwarg)


print("before dec")
def my_decorator(func):
    print("decorator start")
    def wrapper(*args, **kwargs):
        print("wrapper start")
        res = func(*args, **kwargs) * 10
        print("wrapper end")
        return res
    print("decorator end")
    print(type(wrapper))
    print(wrapper)
    return wrapper
print("after dec")

@my_decorator
@my_decorator
def my_foo():
    print("my_foo")
    return 3.14

# my_foo = my_decorator(my_foo)

print(my_foo())
print(dir())

"""
хлеб
сыр
лист салата
колбаса
майонез
хлеб
"""