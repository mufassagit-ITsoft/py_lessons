'''
Docstring for built_in_func.indices: 

Write a Python program that prints the character at index i 
in the string s.

If the index is out of range, 
the program should print "i out of range"

If the string is empty, the program should print "Empty String"
'''

py_str = "Hello"
i = 4

if len(py_str) == 0:
    print("Empty String")
elif i < len(py_str):
    print(py_str[i])
else:
    print("i out of range")