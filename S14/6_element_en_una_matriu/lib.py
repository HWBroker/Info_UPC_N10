# NoMoreHomework

def hi_ha_k(m, k):
    f = False
    for i in m:
        if not f:
            for j in i:
                if j == k:
                    f = True
                    break

    return f
