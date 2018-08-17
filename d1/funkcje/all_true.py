def all_true(l):
    b = True
    for el in l:
        b = b and el
    return b

def all_true2(l):
    return sum(l) == len(l)