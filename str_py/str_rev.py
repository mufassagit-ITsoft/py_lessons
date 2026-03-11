'''
Docstring for str_rev.py

Write a Python program that reverses the individual words in the 
string s and changes their capitalization. Uppercase letters 
should be printed in lowercase and vice versa.

Assume that the string only contains letters and spaces are 
used to separate words.
'''

str_py = input(str("Enter the word or a sentence: "))
str_rev = ""

str_list = str_py.split()
# split is used to create a list out of a string. It splits them into
# words.
for word in range(len(str_list)):
    str_new = str_list[word][::-1].swapcase()
    str_rev += str_new + " "
str_rev.rstrip()

print(str_rev)

# swapcase method, flips a capital letter to a lower case letter and 
# and lowercase letter to a capital letter.