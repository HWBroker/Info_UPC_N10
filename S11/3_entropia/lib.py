# NoMoreHomework

# Avís: La formula de l'enunciat no és correcta. Aquest script dona incorrecte.

from math import log2

def freq(v, x):
    f = 0

    for i in v:
        if i == x:
            f += 1

    return f/len(v)

def entropia(v):
    h = 0

    for i in range(len(v)):
        f = freq(v, v[i])
        h += f*log2(f)
        print(f"{f}*{log2(f)} = {f*log2(f)}")
        print(h)
    
    return -h

