# NoMoreHomework

def main():
    n = int(input())
    x = int(input())
    k = 0
    fk = 1
    s = 0

    while k <= n:
        if k == 0:
            fk = 1
        else:
            fk *= k

        s += (x+(2*k))/fk

        k += 1

    print(s)

if __name__ == '__main__':
    main()
