dict_a = {"a":4, "b":6}
key_ch = "b"

def is_key(dict_a, key_ch):
    if key_ch in dict_a:
        print(True)
    else:
        print(False)   
is_key(dict_a, key_ch)

#alternate but efficient
print(key_ch in dict_a)