# NoMoreHomework

def main():
    i = int(input())
    j = int(input())
    k = int(input())
    f = True

    while k != 0:
        if not (k >= i and k <= j):
            f = False
        k = int(input())

    print(f)

if __name__ == '__main__':
    main()
