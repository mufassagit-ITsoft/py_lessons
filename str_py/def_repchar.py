str1 = "python"

def rep_char(str1):
    rep_charli = []
    sort_li = sorted(str1)
    total = 0
    for char in sort_li:
        if sort_li.count(char) > 1:
            rep_charli.append(char)
            set_li = list(set(rep_charli))
            total += 1
    return set_li, total

print(rep_char(str1))   