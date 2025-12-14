'''
Docstring for str_py.slice_str

The objective of this python exercise is to take the first three
and the last three characters and combine them into one string, without
using the characters in between the first and the last three characters
of the string. 

Input : Thunderous
Output : Thuous

If the string < 6 characters, the code should return "".

'''

str_py = input("Enter the string: ")
if len(str_py) >= 6:
    sliced_str = str_py[:3] + str_py[-3::]
    print(sliced_str)
else:
    print("")

'''
T    h  u  n  d  e  r  o  u  s
0    1  2  3  4  5  6  7  8  9
-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

Knowing that the objective is to combine the first three and the
last three characters of the original string into one new string, 
this method should work. 
'''

# alternative code
if len(str_py) >= 6:
    sliced_str = str_py[:3] + "" + str_py[len(str_py)-3:]
    print(sliced_str)
else:
    print("")

# optimized code version
char_num = int(input("Enter the character limit (qty): "))

if len(str_py) > char_num*2:
    new_str = str_py[:char_num] + str_py[len(str_py)-char_num:]
    print(new_str)
else:
    print("")

# This code is preferable, as this is less error prone