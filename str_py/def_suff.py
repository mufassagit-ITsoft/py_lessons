str1 = "Stagnation"
suffix = "tion"
def pref_char(str1, suffix):
    for elem in str1:
        if suffix in str1:
            return True
        else:
            return False
            
print(pref_char(str1, suffix))