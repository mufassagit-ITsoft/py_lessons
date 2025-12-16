'''
Docstring for str_py.slic_str2
The challenge here is to print out the charcters at the even 
indices of a sliced string. 

input = "Thunderous"
output = "hneos"

If the string is empty or has one charcter, the result should be 
printed as "" or print without any changes. 
'''

str_py = input("Enter a word: ")
new_str = ""
new_str2 = ""

for char in range(len(str_py)):
    if char%2 != 0:
        new_str += str_py[char]
    elif len(str_py) < 2:
        new_str += str_py
print(new_str)

# For indices, to get to the even index, the logic must not equal
# to zero.

# alternative code

for i in range(1, len(str_py), 2):
    new_str2 += str_py[i]
print(new_str2)

# This does the same as the for for loop on range() and len()
# The difference is in the use of conditional logic.