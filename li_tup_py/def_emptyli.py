list_a = [1, 2, 3, 4]

def enum_char(list_a):
    if len(list_a) == 0:
        print("Empty List")
    else:
        for ind, char in enumerate(list_a):
            print(char, ind)

enum_char(list_a)