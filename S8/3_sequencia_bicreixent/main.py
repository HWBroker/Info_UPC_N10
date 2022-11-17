# NoMoreHomework

'''

AVÍS! AQUEST EXERCICI NO ES POSSIBLE.

Ho he intentat de manera "legal" no ho he pogut conseguir.

Ho he intentat amb el mètode seguent que no pot fallar (matemàticament, és exactament el que descriu el problema.) i el test privat segueix donant malament.

'''

def main():
    s1 = []
    s2 = []
    
    i = int(input())
    c = 0

    while i != -1:
        if c % 2 == 0:
            s1.append(i)
        else:
            s2.append(i)
        c += 1
        i = int(input())
    
    ss1 = s1.copy()
    ss1.sort()

    ss2 = s2.copy()
    ss2.sort()
    
    if ss1 != s1 or ss2 != s2 or s1[0] > s2[-1]:
        print(False)
    elif len(s1) < 2 or len(s2) < 2 or len(s1) != len(s2): 
        print(False)
    else:
        print(True)

if __name__ == '__main__':
    main()
