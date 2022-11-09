# NoMoreHomework

def main():
    i = int(input())
    j = 2
    k = 2
    f = False
    

    while j <= i:
        while k < j:
            if ((j/k) % 1) == 0:
                f = True
                break
            k += 1
        k = 2

        if not f and j != i:
            print(j)

        f = False
        j += 1

if __name__ == '__main__':
    main()
