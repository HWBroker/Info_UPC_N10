# NoMoreHomework

def main():
    i = int(input())
    pi = i
    c = 0

    while i != 0:
        if i != pi:
            print('(',pi,':',c,') ')
            c = 1
        else:
            c += 1
        pi = i
        i = int(input())
    
    print('(',pi,':',c,') ')



if __name__ == '__main__':
    main()
