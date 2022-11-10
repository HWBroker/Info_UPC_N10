# NoMoreHomework

def main():
    i = int(input())
    p = 0
    n = 0

    while i != 0:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1

        i = int(input())

    print(p > n)

if __name__ == '__main__':
    main()
