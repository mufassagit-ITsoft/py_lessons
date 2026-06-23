str1 = "123456"

def is_numeric(str1):
    if str1.isdecimal():
        return True
    else:
        return False

print(is_numeric(str1))