# NoMoreHomework

def pes_maxim(v,M):
    # Ordena el vector de mes petit a mes gran
    v.sort()
    s = 0

    # Capgira el vector
    j = []
    i = len(v) - 1

    while i >= 0:
        j.append(v[i])
        i -= 1
    
    # Suma els M primers (els M mes grans)
    for k in range(M):
        s += j[k]

    return s
