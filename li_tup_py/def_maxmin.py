list_a = [1, 2, 3, 4]

def max_min(list_a):
    max_val = max(list_a)
    min_val = min(list_a)
    return max_val, min_val

def maxmin_val():
    if list_a == []:
        print([])
    else:
        for val in max_min(list_a):
            print(val, end=" ")

maxmin_val()