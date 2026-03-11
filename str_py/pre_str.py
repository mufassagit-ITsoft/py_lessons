'''
Docstring for str_py.pre_str

Write a Python program that checks if the string s starts with the 
sequence of characters denoted by the variable prefix.If it does, 
print True. Else, print False.
This test should be case sensitive. For example, 
"A" should not be equivalent to "a".

If the length of the prefix is greater than the length of the string, 
print False.

'''
str_py = input(str("Enter a word: "))
str_pre = input(str("Enter the words prefix: "))
is_pre = False

for char in range(len(str_py)):
    if str_pre == str_py[:len(str_pre)]:
        is_pre = True
print(is_pre)

# alt solution, optimal solution
print(str_py[:len(str_pre)] == str_pre)

# alt solution 2, optimal solution
s = str_py.startswith(str_pre)
print(s)
