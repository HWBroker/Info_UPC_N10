# NoMoreHomework

def pot(b, e):
    r = 1
    if e == 0:
        return 1
    elif e == 1:
        return b
    else:
        while e > 0:
            r = r*b
            e -= 1
        return r


def main():
    n = int(input())
    x = int(input())
    k = 0
    s = 0

    while k < n:
        s += (pot(x,k)/pot(2,k))
        k += 1

    print(s)
if __name__ == '__main__':
    main()
