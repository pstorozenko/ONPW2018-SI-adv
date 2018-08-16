def rever1(l):
    nl = []
    for i in range(len(l)):
        nl.append(l[len(l)-i-1])
    return nl


def rever2(l):
    nl = []
    for i in range(len(l) - 1, -1, -1):
        nl.append(l[i])
    return nl


def rever3(l): 
    return list(reversed(l))

