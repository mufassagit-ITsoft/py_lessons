inp = "Coding"

def even_char(inp):
    out = ""
    for elem in range(len(inp)):
        if elem%2 == 0:
            out += inp[elem]
    return out

print(even_char(inp))