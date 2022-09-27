#NoMoreHomework

def main():
    j = int(input())
    flag = False

    for i in range(2, j):
        if j % i == 0 and i % 2 != 0 and i < 10:
            flag = True
            break

    print(flag)

if __name__ == '__main__':
    main()
