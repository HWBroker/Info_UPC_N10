#NoMoreHomework

def main():
    i = int(input())
    j = int(input())
    k = input()

    if k == '+':
        print(f"{i + j}")
    elif k == '-':
        print(f"{i - j}")
    elif k == '*':
        print(f"{i * j}")
    elif k == '/':
        print(f"{i / j}")

if __name__ == '__main__':
    main()
