# NoMoreHomework

def main():
    n = int(input())
    i = int(input())
    c = 0

    while i != 0:
        if i == n:
            c += 1
        i = int(input())

    print(c)
    

if __name__ == '__main__':
    main()
