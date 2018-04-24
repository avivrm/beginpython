# Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world
# Hint: In case of input data being supplied to the question, it should be assumed to be a console input.

counter = int(input('how many number you will enter : '))
arr=[]
for i in range(1, counter+1, 1):
    arr.insert(i,input('Enter the word : '))

list.sort(arr)
print(arr)