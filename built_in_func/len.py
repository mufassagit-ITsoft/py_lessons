''' 
len(object, /)
Return the length (the number of items) of an object. The argument 
may be a sequence (such as a string, bytes, tuple, list, or range) 
or a collection (such as a dictionary, set, or frozen set).

CPython implementation detail: 
len raises OverflowError on lengths larger than sys.maxsize, 
such as range(2 ** 100).
'''

py_str = "Prodhan"
# Result: 7

print(f"py_str = {len(py_str)} letters long")

py_str0 = ""
# Result: 1 from 0

print(f"py_str_0 = {len(py_str0)} letters long")

py_str1 = "P"
# Result: 1

print(f"py_str_1 = {len(py_str1)} letters long")