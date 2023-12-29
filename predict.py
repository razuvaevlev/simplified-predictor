import re
from argparse import ArgumentParser, FileType


# Class for variable options in block of code
class Option:
    def __init__(self, parent):
        # List of variable options
        self.__value = []
        # Parent block of code
        self.__parent = parent

    # Append possible value
    def append(self, value):
        self.__value.append(value)

    # Getter for parent block
    def get_parent(self):
        return self.__parent

    # Getter for variable options
    def get_value(self):
        return self.__value

    # Predict value
    def get_prediction(self):
        result = []
        for value in self.__value[::-1]:
            # If value is an Option block
            # find it's possible values
            if isinstance(value, Option):
                result += value.get_prediction()

            # Else it's an assignments,
            # and it reassigns all previous values(break)
            else:
                result.append(value)
                break
        return result


if __name__ == "__main__":
    # Gets source file from command line arg
    parser = ArgumentParser(description="Simplified Java variables predictor")
    parser.add_argument("file", type=FileType("r"),
                        help="Source Java file")
    source_file = parser.parse_args().file

    # Creates main Option to choose from
    start = Option(None)
    # Current Option which starts at main
    current = start

    # Skipping everything until "int x;"
    while not (re.search(r'int \w', source_file.readline())):
        pass

    # For every line of source code
    for line in source_file.readlines():
        # Check for assignments to variable x("x = n")
        expression = re.search(r'\w ?= ?([0-9]+)', line)
        # Create new sub Option and make it current
        if "if" in line:
            tmp = Option(current)
            current.append(tmp)
            current = tmp

        # Append possible value to Option
        if expression:
            current.append(expression.group(1))

        # Close Option when if-clause closed
        if "}" in line:
            if current.get_parent() is not None:
                current = current.get_parent()
        # Break at the end of the method
        if "System.out.println" in line:
            break

    print(*start.get_prediction())
