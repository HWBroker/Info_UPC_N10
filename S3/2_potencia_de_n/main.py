#NoMoreHomework

def main():
    i = int(input())
    j = 1
    k = 0

    while True: 
        k += 1
        j *= i

        if j >= 20000:
            break

    print(k)


if __name__ == '__main__':
    main()
