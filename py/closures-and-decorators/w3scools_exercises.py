import functools
def logger(func):
  @functools.wraps(func)
  def wrapper(*args,**kwargs):
    print(f"arguments of this function are:{args}")
    print(f"keyword arguments of this function are:{ key,value for key,value in kwargs}")
    return_value=func(*args,**kwargs)
    return return_value
  return wrapper
  