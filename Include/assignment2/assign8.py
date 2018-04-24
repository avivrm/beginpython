# Write a list comprehension statement to generate a list of all pairs of odd positive
# integer values less than 10 where the first value is less than the second value.

arr = [1, 2, 3, 4, 5, 6, 7]

result = [(x, y) for x in arr for y in arr if (x != y and ((x+y) % 2 != 0) and (x+y) < 10)]
print(result)
