# NoMoreHomework

def maxim_suma_columnes(m):
    s = []
    sm = 0
    c = 0
    
    for i in range(len(m[0])):
        s.append(0)
        for j in range(len(m)):
            s[i] += m[j][i]

    for k in range(len(s)):
        if s[k] > sm:
            sm = s[k]
            c = k

    return sm, c
