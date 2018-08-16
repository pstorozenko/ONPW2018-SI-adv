def cs_sort(l, k):
    nl = [0] * k
    for el in l:
        nl[el] += 1
    rl = []
    for i in range(k):
        for j in range(nl[i]):
            rl.append(i)
    return rl