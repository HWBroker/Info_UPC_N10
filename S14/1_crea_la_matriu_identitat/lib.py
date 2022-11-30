# NoMoreHomework

def crea_matriu_identitat(n):
    m = []
    for i in range(n):
        f = []
        for _ in range(n):
            f.append(0)
        f[i] = 1
        m.append(f)
    return m
