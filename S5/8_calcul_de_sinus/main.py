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
    sin = x
    f = False

    xen = x
    xfactn = 1

    while i < n:
        xen *= x*x
        xfactn = fact(i*2+1)
        if not f:
            sin -= (xen)/(xfactn)
            f = True
        else:
            sin += (xen)/(xfactn)
            f = False
        i += 1

    print(sin)

if __name__ == '__main__':
    main()
