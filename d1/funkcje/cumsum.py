def cumsum(l):
    nl = [0]
    for i in range(len(l)):
        nl.append(nl[-1] + l[i])
    return nl[1:]
