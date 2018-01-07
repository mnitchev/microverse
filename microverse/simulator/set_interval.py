from time import time


def set_interval(dt, start=False):
    """Decorator that executes decorated function on given period of time
    WARNING: If the start flag is set to true everything
    after the declaration of the function wont be executed.
    """
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
