dict_a = {"a": 4, "b": 4, "c": 4}
unique_val = set(dict_a.values())


def check_val(dict_a):
    if dict_a == {}:
        return "Empty"
    for v in unique_val:
        if unique_val == v:
            return True
        else:
            return False
print(check_val(dict_a))