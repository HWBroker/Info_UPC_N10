# NoMoreHomework

def calculs(v):
    avg = 0
    ns = 0
    nb = 0
    ne = 0

    for i in v:
        avg += i 

    if len(v) > 0:
        avg = avg/len(v)

    for i in v:
        if i < avg:
            ns += 1
        elif i > avg:
            nb += 1
        elif i == avg:
            ne += 1

    return ns, nb, ne
