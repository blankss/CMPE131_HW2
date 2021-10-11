def multiply_list(multList):
    """
    Multiplies all of the events in a user inputted list and returns the value.

    If an element in the list is not a valid integer, this function will return the boolean value false.

    Returns
    -------
    int
        If the input is valid, returns the product of all the integers in the list.
    boolean
        False if the input is not valid.
    """
    result = 1
    for x in multList:
        # use isdigit() to check if the element in the list is actually an integer so we do not get an error
        if (str(x)).isdigit(): # referenced help from user usr_11 here: https://stackoverflow.com/questions/33049167/attributeerror-int-object-has-no-attribute-isdigit/48224316 since an integer cannot call isdigit()
            x = int(x)
            result *= x
        else:
            return False
    return result