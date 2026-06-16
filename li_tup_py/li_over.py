list_a = [1, 2, 3, 4, 5]
list_b = [1, 2, 3, 4]
diff_list = []

for elem in list_a:
    if elem not in list_b:
        diff_list.append(elem)

print(diff_list)
