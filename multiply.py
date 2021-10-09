def multiply_list():
    """
    Multiplies all of the events in the list and returns the value
    """
    multStr = input("Input: ")
    result = 1
    multStr = multStr[1:len(multStr) - 2]
    multList = multStr.split(", ")
    for x in multList:
        if isinstance(x, int):
            result *= x
        else:
            return False
    return result

print(multiply_list())