'''
Docstring for sort_char.py

Write a Python program to convert a string s to lowercase, sort 
the characters of each word in alphabetical order, and print the 
resulting string.

You may assume that the string only contains letters and spaces 
to separate the words.

Spaces should be preserved in the final string.
'''

str_py = input(str("Enter a word or a sentence: ")) 
str_new = ""

str_list = str_py.split()

str_sort = []
for word in range(len(str_list)):
    str_lower = str_list[word].lower()
    str_sort.append("".join(sorted(str_lower)))

str_new = " ".join(str_sort)
print(str_new)
    
    
