# NoMoreHomework

def main():
    m = int(input())
    n = int(input())
    i = 1
    f = 1
    fp = 0
    fpp = 0
    t = 0

    while i < n:
        fpp = fp
        fp = f
        f = fp + fpp
        if f >= m and f <= n:
            t += f   
        i += 1

    print(t)

if __name__ == '__main__':
    main()
