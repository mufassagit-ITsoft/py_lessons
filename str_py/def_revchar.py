str1 = "Morphin Time"

def rev_char(str1):
    low_str = str1.lower()
    split_li = low_str.split()
    rev_li = []
    for word in split_li:
        sorted_li = "".join(sorted(word))
        rev_li.append(sorted_li[::-1])
    return " ".join(rev_li)
print(rev_char(str1))