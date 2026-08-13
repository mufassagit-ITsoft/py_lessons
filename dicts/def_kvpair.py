dict_a = {"January": 45, "February": 56, "March": 67}

def dict_insert(dict_a):
    new_key = "April"
    new_val = 67
    if new_key not in dict_a:
        dict_a[new_key] = new_val
    return dict_a
print(dict_insert(dict_a))

'''
The function is designed by its conditional statement to not update the 
dictionary, but add to it. Anytime that a dictionary tries to update, it will
not be able to update an already established key. 
'''