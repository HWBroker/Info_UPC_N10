# NoMoreHomework

def multiple_cinc(m):
    f = False
    for i in m:
        if not f:
            for j in i:
                if j % 5 == 0:
                    f = True
                    break
    return f
