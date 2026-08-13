dict_a = {"a": 1, "b": 2, "c": 3}
dict_b = {"c": 4, "d": 6, "e": 8}

def merge_dict(dict_a, dict_b):
    merged_dict = dict_a | dict_b
    return merged_dict
print(merge_dict(dict_a, dict_b))

'''
The "|" is used to merge two dictionaries. This ensures two things happening:
    1. That the merged dictionary has all the key from both dictionaries.
    2. Any overlapping keys, get updated by its second dictionary values,
    which is why dict_b updates "c" from 3 in dict_a to 4 in dict_b to that
    value in the merged_dict merged dictionar value.
'''