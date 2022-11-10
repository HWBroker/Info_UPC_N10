# NoMoreHomework

def main():
    i = int(input())
    j = 0
    k = 0

    while i != -1:
        if i == 0:
            j += 1
        elif i == 1:
            k += 1
        i = int(input())

    print(j > k)

if __name__ == '__main__':
    main()
