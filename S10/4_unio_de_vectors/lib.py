# NoMoreHomework

def unio(v1, v2):
    u = []
    f = True

    for i in v1:
        for j in u:
            if j == i:
                f = False
        if f:
            u.append(i)
        f = True

    for i in v2:
        for j in u:
            if j == i:
                f = False
        if f:
            u.append(i)
        f = True
    
    u.sort()
    return u
