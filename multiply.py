def multiply_list():
    """
    Multiplies all of the events in a user inputted list and returns the value.

    If an element in the list is not a valid integer, this function will return the boolean value false.
    """
    multStr = input("Input: ")
    result = 1
    multStr = multStr[1:len(multStr) - 1] # need to use slicing to exclude the brackets at either side of the user input
    multList = multStr.split(", ")
    for x in multList:
        # use isdigit() to check if the element in the list is actually an integer so we do not get an error
        if x.isdigit():
            x = int(x)
            result *= x
        else:
            return False
    return result