# NoMoreHomework

def suma_diagonal(m):
    s = 0
    for i in range(len(m)):
        s += m[i][i]
    
    return s
