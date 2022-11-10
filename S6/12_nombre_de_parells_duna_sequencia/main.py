# NoMoreHomework

def main():
    i = int(input())
    c = 0
    while i != 0:
        if i % 2 == 0:
            c += 1
        i = int(input())
    print(c)

if __name__ == '__main__':
    main()
