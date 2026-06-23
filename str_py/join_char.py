str1 = "Pack my box with five dozen liquor jugs"

def join_char(str1):
    str_li = str1.split()
    for elem in str_li:
        new_str = "".join(str_li)
    return new_str

print(join_char(str1))