list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def combo_li(list_a):
    fl = []
    for elea in list_a:
        for eleb in elea:
            fl.append(eleb)
    return fl
print(combo_li(list_a))
        