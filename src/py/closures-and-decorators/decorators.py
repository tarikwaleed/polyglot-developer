import functools
import time


# This formula is a good boilerplate template for building more complex decorators.
def decorator(func):
    @functools.wraps(func)
    # the above line returns the identity of the decorated function
    def wrapper(*args, **kwargs):
        # do something before
        print("awesome thing before")
        # call the function and save the return value
        return_value = func(*args, **kwargs)
        # do something after
        print("awesome thing after")
        # return the saved return value
        return return_value

    return wrapper


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)

    return wrapper_do_twice


def timer_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        return_value = func(*args, **kwargs)
        end_time = time.perf_counter()
        print(
            f"the function {func.__name__} took {end_time-start_time:.1f}sec to finish"
        )
        return return_value

    return wrapper


def slow_down(func):
    """Sleep 1 second before calling the function"""

    @functools.wraps(func)
    def wrapper_slow_down(*args, **kwargs):
        time.sleep(1)
        return func(*args, **kwargs)

    return wrapper_slow_down


def debug(func):

    """Print the function signature and return value"""

    @functools.wraps(func)

    def wrapper_debug(*args, **kwargs):

        args_repr = [repr(a) for a in args]

        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]

        signature = ", ".join(args_repr + kwargs_repr)

        print(f"Calling {func.__name__}({signature})")

        value = func(*args, **kwargs)

        print(f"{func.__name__}() returned {repr(value)}")

        return value

    return wrapper_debug

PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func


def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat