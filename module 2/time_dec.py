import datetime
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = func(*args, **kwargs)
        end_time = datetime.datetime.now()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time}")
        return result
    return wrapper


@measure_time
def some_function():
    time.sleep(2)

some_function()