from collections import defaultdict

def dict_mode(l):
    d = defaultdict(int)
    for el in l:
        d[el] += 1
    vm = 0
    mode = None
    for k, v in d.items():
        if vm < v:
            mode = k
            vm = v
    return mode 
