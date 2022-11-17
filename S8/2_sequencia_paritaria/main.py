# NoMoreHomework

def main():
    _ = int(input())
    ppi = int(input())
    pi = int(input())
    i = int(input())
    l = False
    f = True

    while i != -1:
        if ((i + pi) % 2 != 0) and ppi != pi and pi % 2 != 0:
            f = False
        ppi = pi
        pi = i
        i = int(input())
        l = True

    if l:
        print(f)
    else:
        print(False)

if __name__ == '__main__':
    main()
