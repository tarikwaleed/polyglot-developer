import functools
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