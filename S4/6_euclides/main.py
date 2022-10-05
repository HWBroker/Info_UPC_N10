#NoMoreHomework

def main():
    i = int(input())
    j = int(input())
    
    f = False

    while not f:
        if i == j:
            print(i)
            f = True
        elif i > j:
            i -= j 
        elif i < j:
            j -= i

if __name__ == '__main__':
    main()
