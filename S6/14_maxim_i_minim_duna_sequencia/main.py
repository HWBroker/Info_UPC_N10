# NoMoreHomework

def main():
    i = int(input())
    j = 0
    k = 2147483647
    f = 0

    while i != 0:
        if i > j:
            j = i
        elif i < k:
            k = i

        i = int(input())
        f += 1
    
    if f > 1:
        print(j, k)
    else:
        print(j, j)

if __name__ == '__main__':
    main()
