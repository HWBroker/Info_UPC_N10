# NoMoreHomework

def main():
    n = int(input())
    i = 1
    f = 1
    fp = 0
    fpp = 0
    print(1)

    while i < n:
        fpp = fp
        fp = f
        f = fp + fpp
        print(f)
        i += 1

if __name__ == '__main__':
    main()
