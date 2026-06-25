list_a = [4, 5]

def countnum(list_a):
    count = 0
    for num in range(len(list_a)):
        if list_a[num] > 3:
            count += 1
        else:
            count = 0
    return count
print(countnum(list_a))