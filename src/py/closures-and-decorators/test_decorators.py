from decorators import *



@timer_decorator
def useless_function_that_wastes_some_time():
    sum = 0
    for _ in range(10_000_000):
        sum += _

"""
when the interpter sees the @ sign it behaves in the following way:
    - it creates a new name with the same name of the function and binds to it the decorator function
        countdown=register(countdown)
    - it executes the decorator function if there is any code inside it other than the return
    - now, the function is decorated and when you call it , the actual function that is executed
    is the function returned by the decorator
"""
@register
def countdown(from_number):
    if from_number < 1:
        print("Liftoff!")
    else:
        print(from_number)
        countdown(from_number - 1)

@register
def say_hello(name):
    return f"Hello {name}"


@register
def be_awesome(name):
    return f"Yo {name}, together we're the awesomest!"

# import pprint
# pprint.pprint(PLUGINS)

import random

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    # this is the same as
    print(f"Using {repr(greeter)}")
    return greeter_func(name)


@repeat(10)
def say_hello():
    print("Hello")
    return "a"

say_hello()