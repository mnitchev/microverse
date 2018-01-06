from time import time


def set_interval(dt, start=False):
    def decorator(func):
        def wrapper():
            start_time = time()
            while True:
                if (time() - start_time > dt):
                    start_time = time()
                    func()
        if start:
            wrapper()
        return wrapper
    return decorator
