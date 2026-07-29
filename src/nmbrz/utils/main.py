# UTILITES FOR NMBRZ PACKAGE

"""
File with alone ultilites for [Utils](./__init__.py)
"""

# timer: to time a function

from time import time

def timer(func):
    """
    Timer utility for functions
    """

    def wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        time_taken = end_time - start_time
        str_args = f"{args if args else ''}{', ' if args and kwargs else ''}{kwargs if kwargs else ''}"
        func_repr = f"{func.__name__}({str_args})"
        print(f"Function {func_repr} executed in {time_taken} seconds")
        print("Result:", result)
        return result
    wrapper()
    return wrapper
