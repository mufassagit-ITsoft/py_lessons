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

py_str = input("Enter a word: ")
target_str = input("Enter a target character to replace: ")
repl_str = input("Enter a replacement character for the new word: ")

for char in range(len(py_str)):
    if target_str in py_str:
        new_str = py_str.replace(target_str, repl_str)
    else:
        new_str = py_str

if py_str != new_str:
    print(new_str)
else:
    print(f"No such character or letters exist in the word or sentence for {py_str}")
    

