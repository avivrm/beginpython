# Use filter to eliminate all words that are shorter than 4 letters from a list of words

arr = ['hello', 'how', 'are', 'you', 'inside']

result  = [word for word in arr if len(word)>4]
print(result)