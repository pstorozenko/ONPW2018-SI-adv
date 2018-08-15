def cumsum(l):
    nl = []
    for i in range(len(l)):
        nl.append(sum(l[0:i+1]))
    return nl
