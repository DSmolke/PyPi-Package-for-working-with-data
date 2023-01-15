from typing import Callable, Any


def to_upper(func: Callable[[Any], str]):
    """ Higher order function that changes argument function return value to uppercase """
    def wrapper(*args, **kwargs) -> str:
        return func(*args, **kwargs).upper()
    return wrapper

def to_lower(func: Callable[[Any], str]):
    """ Higher order function that changes argument function return value to lowercase """
    def wrapper(*args, **kwargs) -> str:
        return func(*args, **kwargs).lower()
    return wrapper

def to_char_list(func: Callable[[Any], str]):
    """ Higher order function that changes argument function return value list of str-s containing only one character """
    def wrapper(*args, **kwargs) -> str:
        return list(func(*args, **kwargs))
    return wrapper


