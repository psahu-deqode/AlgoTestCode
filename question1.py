""" Function for string comprehension """
from itertools import groupby


# function for string comprehension
def compress(string):
    # grouped elements by the help of keys and found the count
    count_list = [key + str(len(list(group))) for key, group in groupby(string)]
    new_str = ''
    for i in count_list:
        if int(i[1]) == 1:
            i = i[0]
        new_str += i
    return new_str


# Take the string as user input

string = input('Please enter the string you want to compress ')
print(compress(string))
