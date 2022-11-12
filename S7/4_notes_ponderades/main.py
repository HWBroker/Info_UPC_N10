# NoMoreHomework

def main():
    c = float(input())
    p = int(input())
    t = 0

    while p > 0:
        t += float(input())*float(input())
        p -= 1

    print(t/c)

if __name__ == '__main__':
    main()
