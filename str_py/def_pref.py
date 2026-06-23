str1 = "Stagnation"
prefix = "stag"
def pref_char(str1, prefix):
    for elem in str1:
        if prefix in str1.casefold() or str1.upper():
            return True
        else:
            return False
            
print(pref_char(str1, prefix))