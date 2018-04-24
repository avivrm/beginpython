# Use filter to determine the percentage of Fahrenheit temperatures in a list are within the range 32 to 80

arr = [23, 34, 55, 66, 77, 88, 99, 85]

filterArr = [x for x in arr if (x >= 32 and x <= 80)]
print(filterArr)

