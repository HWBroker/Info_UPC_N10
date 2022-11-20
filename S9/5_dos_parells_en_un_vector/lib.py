# NoMoreHomework

def dosparells(v):
    f = False
    c = 0
    for i in v:
        if i % 2 == 0:
            c += 1
        if c > 1:
            f = True
            break # Aquest break no es necessari, però fa el programa mes ràpid
    return f
