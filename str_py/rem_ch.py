str1 = "Help"
n = 2

def rem_char(str1):
    if len(str1) == 0 or n >= len(str1):
        print(str1)
    else:
        new_str = ""
        for elem in range(len(str1)):
            if elem != n:
                new_str += str1[elem]
        print(new_str)

print(rem_char(str1))