'''
Docstring for count_py.py

Write a Python program to count the number of repeated characters 
in the string s.

The program must print the total number of repeated characters and 
a message on the next line displaying the repeated characters s
eparated by a space and sorted alphabetically.

If there are no repeated characters in the string, print 0 as the 
total count and None on the next line.
'''

str_py = input(str("Enter the word or a sentence: "))
str_char = input(str("Enter the character to be counted: "))

count = 0
for char in range(len(str_py)):
    if str_py[char] == str_char:
        count += 1

print(count)