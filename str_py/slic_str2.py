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

for char in range(len(str_py)):
    if char%2 != 0:
        new_str += str_py[char]
print(new_str)