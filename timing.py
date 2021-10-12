import time

def calculate_time(func):
    """"
    Wraps the func with the wrapper to calculate the runtime and print it out.

    Parameters
    ----------
    func: the function to wrap timer around.
        The value to pass into the function to time.
    """
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        print(f"Total time {end - start}")
    return wrapper