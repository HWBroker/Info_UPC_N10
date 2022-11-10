# NoMoreHomework

def main():
    i = int(input())
    j = 0
    c = 0
    
    while i != 0:
        j += i
        c += 1
        i = int(input())

    if c > 0:
        print(j/c)
    else:
        print(0)

if __name__ == '__main__':
    main()
