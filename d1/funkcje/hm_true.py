def hm_true1(l):
    c = 0
    for el in l:
        if el == True:
            c += 1
    return c

def hm_true2(l):
    return sum(l)