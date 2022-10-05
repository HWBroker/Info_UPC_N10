#NoMoreHomework

def main():
    i = int(input())
    j = 1
    k = 1

    while i >= j:
        print(k)
        j += 1

        if j > i:
            break

        print(i + 1 - k)
        j += 1
        k += 1


if __name__ == '__main__':
    main()
