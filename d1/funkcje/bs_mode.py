from min_max_arg import min_max_arg

def bs_mode(l, k):
    nl = [0] * k
    for el in l:
        nl[el] += 1
    _, ima = min_max_arg(nl)
    return ima

