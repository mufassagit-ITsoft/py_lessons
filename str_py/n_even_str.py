'''
Docstring for str_py.n_even_str
In this exercise, the point is to remove a substring from even 
indices, that result in the remaining substring as the new string.
'''

str_py = "Wrestling"
new_str = ""

for char in range(len(str_py)):
    if char%2 != 0:
        new_str += str_py[char]
print(new_str)