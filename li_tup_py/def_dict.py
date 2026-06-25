list_a = ["a", "a", "b", "c", "a", "b"]

def list_dict(list_a):
    char_dict = {}
    for char in list_a:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict
print(list_dict(list_a))