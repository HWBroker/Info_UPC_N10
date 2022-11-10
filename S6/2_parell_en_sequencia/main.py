# NoMoreHomework

def main():
    f = False
    i = int(input())
    while i != 0:
        if i % 2 == 0:
            f = True
        i = int(input())

    print(f)

if __name__ == '__main__':
    main()
