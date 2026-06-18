inp = "Pneumonoultramicroscopicsilicovolcanoconiosis"
n = len(inp) - 4

def first_last(inp):
    output = ""
    if len(inp) < 6:
        print("")
    else:
        output = inp[:4] + inp[n:]
        print(output)
    
print(first_last(inp))