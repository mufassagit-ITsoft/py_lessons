'''
Docstring for str_py.n_str
The output for this program would be where a string is stated by
its index within the range of the string length. If the string index is
out of range or empty, then the output is where the input is in tact. If
the string is withint the range of the length, then the output is the
string without the n stated.

input = "Wales"
n = 2
output = "Waes"
'''

str_py = input("Enter the word: ")
print(f"The length of {str_py} is {len(str_py)}")
ind = int(input("Enter the index from the word to omit: "))

if (len(str_py) == 0) or (ind >= len(str_py)):
    print(str_py)
else:
    new_str = ""
    for char in range(len(str_py)):
        if char != ind:
            new_str += str_py[char]
    print(new_str)
