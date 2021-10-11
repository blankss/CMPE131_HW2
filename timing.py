import time

def my_decorator(func):
    def wrapper(func):
        x = func()
        time.sleep(2)
        y = func()
        # help from https://realpython.com/python-f-strings/ for f strings
        print(f"Total time: {y - x}")
    return wrapper

def calculate_time():
    # help from https://realpython.com/primer-on-python-decorators/#simple-decorators for decorators
    x = time.time()
    return x

calculate_time = my_decorator(calculate_time)
calculate_time()