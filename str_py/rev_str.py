'''
Docstring for rev_str: 
This is an exercise in reversing a string. So "Hello" would have to
result as "olleH"
'''

str_py = "Star Trek"
rev_str = str_py[::-1]
print(rev_str)

str_py = "Star Trek"
rev_str = str_py[::-1].lower()
print(rev_str)
# note:
# lower() is used to convert all capital letters in a string to 
# uppercase.

str_py1 = "Star"
rev_str1 = str_py1[::-1]
print(rev_str1)

str_py2 = "Trek"
rev_str2 = str_py2[::-1]
print(rev_str2)

str_py_emp = ""
rev_str3 = str_py_emp[::-1]
print(rev_str3)
# note: makes sense, as this is an empty string.

#alternative code
rev_str4 = "".join(reversed(str_py))
print(rev_str4)

'''
Two things to note. 
1. The use of the join() means that it is taking the string,
just concatenating them together via this built in function.

2. The use of reversed(var) means that the var or variable used
in the function often yieds to the string being reverse. It is used
more as an iterator over the elements of an iterable. In this case, 
a string is an iterable. 

3. The way to read this code, would be that, the string got reversed
using the reversed(var). Then the join() is being used on top of the 
reversed() to then ensure that the string is concatenating to form the
reversed word of str_py variable. 

4. rev_str4 == rev_str1
'''

word = "word"
rev_word = reversed(word)
print(rev_word)

# If the reversed(var) is used, then it yields the result as 
# the space of the address of the memory on the machine that
# is being used. Therefore, it is best to use it on a helper 
# function such as join() or others.