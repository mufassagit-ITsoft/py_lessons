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
count = 0
str_char = []

for char in str_py.lower():
    if (str_py.count(char) > 1) and (char not in str_char):
        count += 1
        str_char.append(char)

if len(str_char) > 0:
    for char in sorted(str_char):
        print(char, end=" ")
else:
    print(None)

print("\n")
print(count)

# alt solution, can be useful
# keep the first for loop and run a new conditional statement
if str_char:
    print(*sorted(str_char), sep=" ")
else:
    print(None)
print(count)

#alt soution 2, 
for char in str_py.lower():
    if (str_py.count(char) > 1) and (char not in str_char):
        str_char.append(char)
print(len(str_char))

if str_char:
    print(*sorted(str_char), sep=" ")
else:
    print(None)