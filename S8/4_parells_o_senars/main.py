# NoMoreHomework

def main():
    i = int(input())
    p = 0
    s = 0

    while i != -1:
        if i % 2 == 0:
            p += i 
        else:
            s += i 

        if p > s:
            print('P')
        elif s > p:
            print('S')
        else:
            print('X')

        i = int(input())

if __name__ == '__main__':
    main()
