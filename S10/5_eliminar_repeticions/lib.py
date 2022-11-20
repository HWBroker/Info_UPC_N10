# NoMoreHomework

def uniq(v):
    f = True
    u = []

    for i in v:
        for j in u:
            if j == i:
                f = False
        if f:
            u.append(i)
        f = True

    u.sort()
    return u
