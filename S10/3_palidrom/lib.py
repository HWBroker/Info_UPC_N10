def espalindrom(v): 
    j = []
    i = len(v) - 1

    while i >= 0:
        j.append(v[i])
        i -= 1

    return v == j
