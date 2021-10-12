import time

def calculate_time(func):
    def wrapper():
    """"
    Wraps the func with the wrapper to calculate the runtime and print it out.

    Parameters
    ----------
    func: the function to wrap timer around.
        The value to pass into the function to time.
    """
    # help with decorators from https://realpython.com/primer-on-python-decorators/
    start = time.time()
    func(*args) #still need to execute the function so we sandwich it between start and end to time it
    end = time.time()
    # help from https://realpython.com/python-f-strings/ for f strings
    print(f"Total time: {end - start}")
return wrapper