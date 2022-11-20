# NoMoreHomework

def iguals(v):
    if len(v) > 1:

        pi = v[0]
        i = 1
        f = True

        while i < len(v) and f:
            if v[i] != pi:
                f = False
            else:
                pi = v[i]
                i += 1

        return f
    else:
        return True
