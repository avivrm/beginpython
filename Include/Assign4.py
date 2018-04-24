# Write a program which accepts a sequence of comma-separated numbers from console and generate a list
# and a tuple which contains every number.
# Suppose the following input is supplied to the program:
# 34,67,55,33,12,98
# Then, the output should be:
# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# Hint:In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple

totalVal = int(input('enter total numbers : '))
list = []

for i in range(1,totalVal+1):
    val = input('enter the number : ')
    list.insert(i,val)


print(list)
print(tuple(list))
