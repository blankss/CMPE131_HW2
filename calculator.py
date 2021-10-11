def parse_input():
    """
    Parses the input and passes the parsed input correctly into the calculator function.

    Returns
    -------
    float

    The calculated float from passing in the parameters of the operands and the operation symbol to calculator.
    """
    inputString = input("Enter equation: ")
    inputList = inputString.split(" ")
    return calculator(inputList[0], inputList[2], inputList[1]) #order is 0, 2, 1 since the middle is the operator, which corresponds with index 1

def calculator(number1, number2, operator):
    """
    Calculates the correct value from the equation that was taken from the user. 

    If the operator or numbers are invalid, the function exits and returns the boolean value false. Valid operators are 
    +, -, *, /, //, and ** which are addition, subtraction, multiplication, division, integer division, and power respectively.

    Parameters
    ----------
    number1: float
        First operand.
    number2: float
        Second operand.
    operator: string
        Operator to do an operation of number1 operator number2.

    Returns
    -------
    float
        The operation of ``number1`` and ``number2``.
    
    Examples
    --------
    Enter equation: 10 + 11
    21.0
    Enter equation: 10 ** 2
    100.0
    """
    try: #use a try and except block to test whether or not we can convert the 2 numbers into floats for valid input
        #https://www.tutorialspoint.com/python/python_exceptions.htm for try except handling help
        number1 = float(number1)
        number2 = float(number2)
    except ValueError:
        return False

    if operator == "+":
        return number1 + number2
    elif operator == "-":
        return number1 - number2
    elif operator == "*":
        return number1 * number2
    elif operator == "/":
        if (number2 == 0):
            return False
        return number1 / number2
    elif operator == "//":
        if (number2 == 0):
            return False
        return number1 // number2
    elif operator == "**":
        return number1 ** number2
    else:
        return False