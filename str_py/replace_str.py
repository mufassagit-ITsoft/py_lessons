'''
Docstring for str_py.replace_str
This exercise takes a substring from a string or a word, and
replaces that substring from that word with a new substring. 

ex:
word = "substring"
target = "u"
replace = "i"
new_word = "sebstring"
'''

py_str = "Klingons"
target_str = "n"
repl_str = "a"

for char in range(len(py_str)):
    if target_str in py_str:
        new_str = py_str.replace(target_str, repl_str)
print(new_str)