# NoMoreHomework

def main():
    i = int(input())
    j = 0
    if i != 0:
        j = int(input())
    f = True

    while (i != 0) and (j != 0):
        if i != j:
            f = False
        i = int(input())

    print(f)

if __name__ == '__main__':
    main()
