# NoMoreHomework

def main():
    k = int(input())
    j = int(input())
    i = int(input())
    c = 0

    while i != -1:
        if k < j > i:
            c += 1
        k = j
        j = i
        i = int(input())
    
    print(c)

if __name__ == '__main__':
    main()
