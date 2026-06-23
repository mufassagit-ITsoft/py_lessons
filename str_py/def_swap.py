str1 = "Python is Great BROTHER!"

def rev_swap(str1):
    for char in str1:
        new_str = str1[::-1]
    return new_str
    
print(rev_swap(str1).swapcase())
