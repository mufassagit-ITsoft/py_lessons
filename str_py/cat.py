'''
Docstring for str_py.cat

Write a Python program that prints a copy of the string without any 
spaces. Words should be connected in the final string.If the string 
doesn't contain spaces, print it intact.

'''
str_py = input(str("Enter a word or sentence: "))
new_str = ""

for char in range(len(str_py)):
    if " " in str_py:
        str_rep = str_py[char].replace(" ", "")
        new_str += str_rep
    else:
        # When its only a word
        new_str += str_py[char]

print(new_str)

# alt solution, optimal solution

str_rep2 = str_py.replace(" ", "")
print(str_rep2)

# alt solution 2

new_str2 = ""
for char in range(len(str_py)):
    if str_py[char] != " ":
        new_str2 += str_py[char]
print(new_str2)