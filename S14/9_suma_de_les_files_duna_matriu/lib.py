# NoMoreHomework

def suma_files(m):
    s = []
    for i in range(len(m)):
        s.append(0)
        for j in range(len(m[0])):
            s[i] += m[i][j]
    return s
