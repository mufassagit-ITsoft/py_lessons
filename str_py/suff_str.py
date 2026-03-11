'''
Docstring for suff_str.py

Write a Python program that checks if the string s ends with a 
specific sequence of characters denoted by the variable suffix.

For the rest of the conditions, check on pre_str.py comments. 

'''

str_py = input(str("Enter a word: "))
str_suff = input(str("Enter the words prefix: "))
is_pre = False

for char in range(len(str_py)):
    if str_suff == str_py[len(str_suff):len(str_py)]:
        is_pre = True
print(is_pre)

# alt solution
print(str_py[len(str_suff):len(str_py)] == str_suff)

# alt solution 2
# -len(str_suff) means '<= -1', which is at the suffix of the string
print(str_py[-len(str_suff):] == str_suff)

# alt solution 3, optimal solution
print(str_py.endswith(str_suff))
