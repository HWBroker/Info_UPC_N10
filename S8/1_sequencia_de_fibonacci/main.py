# NoMoreHomework

def main():
    n = int(input())
    i = 1
    f = 1
    fp = 0
    fpp = 0
    flag = True

    if i != n:
        flag = False

    while n != 0:
        fpp = fp
        fp = f
        f = fp + fpp
        n = int(input())
        if f != n and n != 0:
            flag = False
        i += 1

    print(flag)


if __name__ == '__main__':
    main()
