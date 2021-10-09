def parse_input():
    """
    Parses the input and passes the parsed input correctly into the calculator.
    """
    inputString = input("Enter equation: ")
    inputList = inputString.split(" ")
    calculator(inputList[0], inputList[2], inputList[1]) #order is 0, 2, 1 since the middle is the operator, which corresponds with index 1

parse_input()