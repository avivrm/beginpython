# Use map and a lambda function to convert a list of Fahrenheit temperatures
# to a list of Celsius temperatures

arr = [97, 101, 58, 33, 15]
print(list(map(lambda x: ((x-32)* (0.5556)), arr)))
