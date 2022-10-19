# NoMoreHomework

def main():
    k = int(input())
    j = int(input())
    i = int(input())

    f = True

    while not (i == 0):
        if not (i >= j >= k or i <= j <= k):
            f = False
        k = j
        j = i
        i = int(input())
    print(f)

if __name__ == '__main__':
    main()
