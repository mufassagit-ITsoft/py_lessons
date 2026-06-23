input = "Try harder"
target_elem = "T"

def ind_str(input):
    if len(input) == 0:
        return 0
    elif target_elem not in input:
        return f"{target_elem} is out of range"
    else:
        inp_ind = []
        for ind, elem in enumerate(input):
            if target_elem == elem:
                inp_ind.append(ind)
                print(ind, end=" ")
print(ind_str(input))
