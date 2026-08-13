dict_a = {"a":4, "b":3, "c":7}

def max_dict(dict_a):
    if dict_a== {}:
        return None
    else:
        max_val = max(list(dict_a.values()))
        return max_val

print(max_dict(dict_a))

def min_dict(dict_a):
    if dict_a== {}:
            return None
    else:
        min_val = min(list(dict_a.values()))
        return min_val

print(min_dict(dict_a))