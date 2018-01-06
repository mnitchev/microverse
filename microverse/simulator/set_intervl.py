from time import time

def set_interval(dt, start=False):
  def decorator(func):
    def wrapper():
      start = time()
      while True:
        if (time() - start > dt):
          start = time()
          func()
    if start:
      wrapper()
    return wrapper
  return decorator
