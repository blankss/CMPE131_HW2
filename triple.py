def tripler(func):
    """
    Wraps the func with the wrapper function to call parameter func three times.

    Parameters
    ----------
    func: function
        The function to call three times.
    
    Returns
    -------
    function
        Returns the wrapper function that calls func three times.
    """
    def wrapper(*args):
        """
        Calls the parameter func three times with a variable number of parameters.

        Parameters
        ----------
        *args: any values
            A variable number of parameters to pass into func.
        """
        # help with args/kwargs from https://realpython.com/python-kwargs-and-args/
        func(*args)
        func(*args)
        func(*args)
    return wrapper