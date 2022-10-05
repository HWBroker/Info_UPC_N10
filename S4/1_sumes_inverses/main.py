#NoMoreHomework

def main():
    i = int(input()) + 1
    
    for j in reversed(range(0, i)):
        k = 0 
        for l in range(0, j+1):
            k += l
        if k > 0:
            print(k)

if __name__ == '__main__':
    main()
