# NoMoreHomework

def main():
    i = int(input())
    j = 0
    f = False

    while i != 0:
        if not f:
            j += 1
        if i < 0:
            f = True
        i = int(input())

    if f:
        print(j)
    else:
        print(-1)

if __name__ == '__main__':
    main()
