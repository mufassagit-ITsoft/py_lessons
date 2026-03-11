'''
Docstring for str_py.sent_str

A pangram is a sentence, phrase, or verse that contains every letter 
of the alphabet at least once. Commonly used to display typefaces, 
test equipment, or practice typing, these "holoalphabetic sentences" 
aim to be as short as possible. The most famous English example is 
"The quick brown fox jumps over the lazy dog".
'''


import string

sent = "The quick brown fox jumps over the lazy dog"

sent_set = set(sent.lower())
if " " in sent_set:
    sent_set.remove(" ")

print(sent_set == set(string.ascii_lowercase))

# ascii_lowercase comes from the string module

# alt solution
is_pangram = True

for char in string.ascii_lowercase:
    if char not in sent_set:
        is_pangram = False

print(is_pangram)

# alt_solution 2

for char in string.ascii_lowercase:
    if char not in sent_set:
        is_pangram = False
        break

print(is_pangram)

# break statement works if the pangram is false at an early point of its
# iteration via the for loop and it can determine that the pangram is false.
# only works if the pangram is false, not true. For true, the for loop
# must be to completion.
