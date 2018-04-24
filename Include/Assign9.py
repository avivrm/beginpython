# Write a program that accepts sequence of lines as input and prints the lines after making
# all characters in the sentence capitalized.
# Suppose the following input is supplied to the program:
# Hello world
# Practice makes perfect
# Then, the output should be:
# HELLO WORLD
# PRACTICE MAKES PERFECT
# Hint : In case of input data being supplied to the question, it should be assumed to be a console input.


totalLines = int(input('How many line will you enter : '))
arr = []
for i in range(0, totalLines):
    arr.append(input('Enter the line : '))

for j in range(0, totalLines):
    print((arr[j]).upper())