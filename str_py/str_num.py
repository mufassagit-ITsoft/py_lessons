'''
Docstring for str_py.str_num
The result should be a boolean result of True or False, when an 
input is a string or an aplphnumberic string, in which the latter
consists of the string with numbers. The object is to get True for
alphanumeric and False for strings only. 

isdecimal() is appropriate for this exercise as it will yield True for
alphnumeric strings and the opposite for strings. 
'''

str_py = input("Enter a word: ")

bool_str = str_py.isdecimal()

print(bool_str)

