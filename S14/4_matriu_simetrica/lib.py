# NoMoreHomework

def matriu_simetrica(m):
    f = True
    
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] != m[j][i]:
                f = False
    return f
