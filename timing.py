import time

def calculate_time(func):
    """"
    Wraps the func with the wrapper function to calculate the runtime and print it out.

    Parameters
    ----------
    func: the function to wrap timer around.
        The value to pass into the function to time.
    
    Returns
    -------
    function
        Returns the wrapper function.
    """
    def wrapper(*args):
        """
        Calculates the time to execute the runtime of func.

        Parameters
        ----------
        *args: any value
            The number of variables to pass into func.
        """
        # help with args/kwargs from https://realpython.com/python-kwargs-and-args/
        # help with decorators from https://realpython.com/primer-on-python-decorators/
        start = time.time()
        func(*args)
        end = time.time()
        print(f"Total time {end - start}") #help with f string from https://realpython.com/python-f-strings/
    return wrapper