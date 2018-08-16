def bin_search(v, x):
    l, r = 0, len(v)
    s = -1
    while l != r:
        s = (l + r) // 2
        if x == v[s]:
            break
        if x < v[s]:
            r = s
        else:
            l = s + 1
    return x == v[s]

n = 10
l = list(range(n))

for i in range(-3,12):
    print('________________')
    print(i)
    print(bin_search(l, i))
    print('________________')