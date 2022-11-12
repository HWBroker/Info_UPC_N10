# NoMoreHomework

def main():
    c = int(input())
    pi = 0
    i = float(input())
    j = 1

    f = False
    
    n = -1

    while c > j:
        if i < 0 and pi < 0 and not f:
            n = j
            f = True
        pi = i
        j += 1
        i = float(input())


    if i < 0 and pi < 0 and not f:
        n = c
        f = True

    if f:
        print(n-1, n)
    else:
        print(-1)

if __name__ == '__main__':
    main()
