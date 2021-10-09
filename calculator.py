def parse_input():
    """
    Parses the input and passes the parsed input correctly into the calculator.
    """
    inputString = input("Enter equation: ")
    inputList = inputString.split(" ")
    calculator(inputList[0], inputList[2], inputList[1]) #order is 0, 2, 1 since the middle is the operator, which corresponds with index 1

def calculator(number1, number2, operator):
    """
    Calculates the correct value from the equation that was taken from the user.

    If the operator or numbers are invalid, the function exits and returns the boolean value false.
    """
    try: #use a try and except block to test whether or not we can convert the 2 numbers into floats for valid input
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
        return number1 / number2
    elif operator == "//":
        return number1 // number2
    elif operator == "**":
        return number1 ** number2
    else:
        return False