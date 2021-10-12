import time

def calculate_time(func):
    """"
    Calculates and prints out the time to execute func.

    Parameters
    ----------
    func: function
        The function to wrap the time wrapper around.

    Returns
    -------
    function
        The wrapped function.
    """
    # help for args/kwargs https://www.geeksforgeeks.org/args-kwargs-python/
    def wrapper(*args):
        """"
        Wraps the func with the wrapper to calculate the runtime and print it out.

        Parameters
        ----------
        *args: any value
            The value to pass into the function to time.
        """
        # help with decorators from https://realpython.com/primer-on-python-decorators/
        start = time.time()
        func(*args) #still need to execute the function so we sandwich it between start and end to time it
        end = time.time()
        # help from https://realpython.com/python-f-strings/ for f strings
        print(f"Total time: {end - start}")
    return wrapper