# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hint :Use __init__ method to construct some parameters


class StringFormat:
   # def __init__(self, str):
    #   self.str = str

    def getString(self):
        self.str = input('Enter the word : ')

    def printString(self):
        print(self.str.upper())

obj = StringFormat()
obj.getString()
obj.printString()
