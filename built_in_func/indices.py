'''
Docstring for built_in_func.indices: 

Write a Python program that prints the character at index i 
in the string s.

If the index is out of range, 
the program should print "i out of range"

If the string is empty, the program should print "Empty String"
'''

py_str = "Whas up"

'''
When using only conditional statements to get an index out of the 
string variable, in this case "Hello", there has to be an index 
variable such as 'i=4' to get the fourth index of the string. 
H e l l o
0 1 2 3 4
(i = 4) == o 
'''
i = 4

if len(py_str) == 0:
    print("Empty String")
elif i < len(py_str):
    print(py_str[i])
else:
    print("i out of range")

print("---------------------------------")
'''
A for loop will only give you each index of the string per loop
variable. So it will yield, H per line, e per line, l per line, 
l per line, and o per line"
'''

for i in range(len(py_str)):
    if len(py_str) == 0:
        print("Empty String")
    elif i < len(py_str):
        print(py_str[i])
    else:
        print("i out of range")
print("---------------------------------")

'''
A while loop can control the loop of the index for a specific index 
being asked for. In this case, as long as the index being stated is 
within the range, you will get the correct response. If out of range, 
the error on the else clause should be stated as a response.
'''

while py_str:
    print("Choose a " + str(range(len(py_str))) + " for the string.")
    index = input("index: ")
    if not py_str:
        print("Empty String")
    elif 0 <= int(index) < len(py_str):
        print(py_str[int(index)])
    else:
        print(f"{index} is out of range. Needs to be between 0 and {len(py_str)}")
    break
print("---------------------------------")

'''
note: range(0,5) means that 5 is the cutoff, between the 0 and 5.
So 5 would be out of range, and therefore, the numbers to choose would
be from 0 to 4, where 5 is the cutoff number. 
'''