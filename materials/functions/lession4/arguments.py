def func_without_arg_without_return():
    """
    :return: None

    >>> func_without_arg_without_return()
    Hello!
    """
    print("Hello!")

def func_with_return() -> int:
    """
    :return: int

    >>> func_with_return()
    10
    """
    return 10

def func_with_one_arg(a: int):
    """
    :param a: любое число
    :return: None

    >>> func_with_one_arg(15)
    30
    """
    print(a * 2)

def func_with_two_args(a: int, b: float) -> float:
    """
    :param a: любое число
    :return: None

    >>> func_with_two_args(5, 4.0)
    20.0
    """
    return a * b

def func_with_many_args(*args) -> None:
    """
    :param args: Any
    :return: None

    >>> func_with_many_args(1, 2, 3)
    {'arg_0': (<class 'int'>, 1), 'arg_1': (<class 'int'>, 2), 'arg_2': (<class 'int'>, 3)}
    >>> func_with_many_args('s', None, [])
    {'arg_0': (<class 'str'>, 's'), 'arg_1': (<class 'NoneType'>, None), 'arg_2': (<class 'list'>, [])}
    >>> func_with_many_args()
    {}
    """
    # import typing
    # r: dict[str, tuple[typing.Any, typing.Type]] = dict()
    r = dict()
    for i, arg in enumerate(args):
        r[f"arg_{i}"] = (type(arg), arg)
    print(r)

def func_with_kwargs(**kwargs) -> None:
    """
    :param args: Any
    :return: None

    >>> func_with_kwargs(first=1, second=2, last=3)
    {'first': (<class 'int'>, 1), 'second': (<class 'int'>, 2), 'last': (<class 'int'>, 3)}
    >>> func_with_kwargs(string='s', nonearg=None, list=[])
    {'string': (<class 'str'>, 's'), 'nonearg': (<class 'NoneType'>, None), 'list': (<class 'list'>, [])}
    >>> func_with_kwargs()
    {}
    """
    # import typing
    # r: dict[str, tuple[typing.Any, typing.Type]] = dict()
    r = dict()
    for key, value in kwargs.items():
        r[key] = (type(value), value)
    print(r)
