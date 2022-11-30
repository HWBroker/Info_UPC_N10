# NoMoreHomework

def suma_matrius(m1, m2):
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m1[i][j] += m2[i][j]
    return m1
