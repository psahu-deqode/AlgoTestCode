""" Function for string comprehension """
from itertools import groupby


# function for string comprehension
def compress(string):
    # initialization
    new_str = string[0]
    result = []
    count = 1
    for c in string[1:]:
        if c == new_str:
            count += 1
        else:
            result.append(new_str + str(count))
            count = 1
            new_str = c
    # condition to ignore appending 1 if the string is not compressed
    if count == 1:
        result.append(new_str)
    else:
        result.append(new_str + str(count))
    # list to string conversion
    return ''.join(result)


# Take the string as user input

string = input('Please enter the string you want to compress ')
print(compress(string))
