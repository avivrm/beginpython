# Use map to generate a new list where all values are replaced by their absolute values.
# You don’t need to use a lambda function.


def replaceNum(num):
    if num < 0:
        return abs(num)
    else:
        return num


arr = [-1, 3, 5, 3, 5, 7, 9, 0]
print(list(map(replaceNum, arr)))

