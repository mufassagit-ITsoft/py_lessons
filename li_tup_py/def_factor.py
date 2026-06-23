li_1 = [1, 2, 3, 4, 5]
li_2 = ['a', 'b', 'c', 'd']
factor = 3

def multi_li(li_2, factor):
    for ind, num in enumerate(li_2):
        li_2[ind] = num * factor
    return li_2

print(multi_li(li_2, factor))

def mult_li2(li_1, factor):
    for num in range(len(li_1)):
        li_1[num] *= factor
    return li_1

print(mult_li2(li_1, factor))