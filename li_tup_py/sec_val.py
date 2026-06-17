# Second largest value
list_a = [5, 3, 4, 1, 2]

if len(list_a) > 1:
    sorted_list = sorted(list_a)
    print(sorted_list[-2])
else:
    print(None)

# alt solution (better way)
if len(list_a) > 1:
    rem_dup = set(list_a)
    rem_dup.remove(max(list_a))
    print(max(rem_dup))

# part 2: second smallest value
if len(list_a) > 1:
    sorted_list = sorted(list_a)
    print(sorted_list[1])
else:
    print(None)

# similar alt solution using set with min()
if len(list_a) > 1:
    sorted_list_min = sorted(list_a)
    rem_dup_min = set(list_a)
    rem_dup_min.remove(min(list_a))
    print(min(rem_dup_min))