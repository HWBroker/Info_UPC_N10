# NoMoreHomework

# Avís! Aquest exercici només es pot solucionar amb el semàfor# groc perquè la correcció té un error.

def semiordenat(v):
    if len(v) > 0:
        v1 = []
        v2 = []

        for i in v:
            if i % 2 == 0:
                v1.append(i)
            else:
                v2.append(i)

        v1s = v1.copy()
        v2s = v2.copy()
        v1s.sort()
        v2s.sort()

        return v1 == v1s and v2 == v2s
