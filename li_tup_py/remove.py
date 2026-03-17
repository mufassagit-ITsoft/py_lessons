list_1 = ["a", "b", "c", "d"]
rem_elem = "d"

if len(list_1) == 0:
    print("Empty List")
elif rem_elem not in list_1:
    print("Not Found")
else:
    for elem in range(list_1.count(rem_elem)):
        list_1.remove(rem_elem)
    print(list_1)