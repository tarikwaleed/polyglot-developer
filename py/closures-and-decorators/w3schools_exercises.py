import functools
import time


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"arguments of this function are:{args}")
        return_value = func(*args, **kwargs)
        print(f"the return value of the function is:{return_value}")
        return return_value

    return wrapper


def time_the_function(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        return_value = func(*args, **kwargs)
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"the function took {execution_time:.1f} to finish execution")
        return return_value

    return wrapper


def stringify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        return str(return_value)

    return wrapper


def return_type_converter(datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return_value = func(*args, **kwargs)
            return datatype(return_value)

        return wrapper

    return decorator


CACHE = dict()


def cache(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        CACHE[func.__name__] = return_value
        return return_value

    return wrapper


def int_validator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return_value = func(*args, **kwargs)
        for arg in args:
            if not isinstance(arg, int):
                raise TypeError("all arguments should be integer")
        return return_value

    return wrapper


def condition_validator(validation_function):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if any(not validation_function(arg) for arg in args):
              raise TypeError("arguments type not supported")
            if any(not validation_function(kwarg) for kwarg in kwargs.values()):
                raise TypeError("keyword arguments type not supported")
            return func(*args, **kwargs)
        return wrapper

    return decorator


def retry(max_tries,delay):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(max_tries):
                try:
                    return_value=func(*args,**kwargs)
                    return return_value
                except Exception as e:
                    print(f'an error has occured {e}. Retrying...')
                    time.sleep(delay)
            raise Exception("max numberretries reached")
        return wrapper
    return decorator


# @retry(max_tries=3,delay=1)
# def failure():
#     raise Exception

RATES=dict()
def rate_limiter(limit):
    def decorator(func):
        RATES[func.__name__]=1
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            if RATES[func.__name__]>limit:
                raise Exception("exceeded the number of times you can call this function")
            else:
                RATES[func.__name__]+=1
                return_value=func(*args,**kwargs)
                return return_value
        return wrapper
    return decorator


@rate_limiter(3)
def foo():
    print("hi")
foo()
foo()
foo()