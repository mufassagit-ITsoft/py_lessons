import string

str1 = "Pack my box with five dozen liquor jugs"
is_pangram = True

def is_alpha(is_pangram):
    for char in string.ascii_lowercase:
        if char not in str1.lower():
            is_pangram = False
            break
    return is_pangram
            
print(is_alpha(is_pangram))