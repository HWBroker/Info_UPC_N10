#NoMoreHomework

def main():
    i = int(input())

    for j in range(1, i + 1):
        if i % j == 0:
            print(j)

if __name__ == '__main__':
    main()
