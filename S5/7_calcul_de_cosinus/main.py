# NoMoreHomework

def fact(n):
    fact = 1
    while n > 1:
        fact = fact * n
        n = n - 1
    return fact

def main():
    x = int(input())
    n = int(input())
    i = 1
    cos = 1
    f = False

    xen = 1
    xfactn = 1

    while i < n:
        xen *= x*x
        xfactn = fact(i*2)
        if not f:
            cos -= (xen)/(xfactn)
            f = True
        else:
            cos += (xen)/(xfactn)
            f = False
        i += 1

    print(cos)

if __name__ == '__main__':
    main()
