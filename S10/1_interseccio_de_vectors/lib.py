# NoMoreHomework

def interseccio(v1,v2):
    l = []
    f = True
    for i in v1:
        for j in v2:
            if i == j:
                for k in l:
                    if k == j:
                        f = False
                if f:
                    l.append(j)
            f = True

    l.sort()
    return l
