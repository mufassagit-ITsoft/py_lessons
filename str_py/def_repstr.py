str1 = "Python"
curr_char = "t"
new_char = "x"

def rep_char(str1):
    if curr_char not in str1:
        print(str1)
    else:
        for elem in range(len(str1)):
            if str1[elem] == curr_char:
                new_str = str1.replace(curr_char, new_char)
                return new_str

print(rep_char(str1))