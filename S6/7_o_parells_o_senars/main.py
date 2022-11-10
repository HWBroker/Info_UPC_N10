# NoMoreHomework

def main():
    i = int(input())
    j = False
    pj = j
    k = True
    
    if i % 2 != 0:
        pj = True
    else:
        pj = False
    
    i = int(input())

    if i % 2 != 0:
        pj = j
        j = True
    else:
        pj = j
        j = False

    while i != 0:
        if k:
            if i % 2 != 0:
                pj = j
                j = True
            else:
                pj = j
                j = False

            if j != pj:
                k = False

        i = int(input())
    
    print(k)

if __name__ == '__main__':
    main()
