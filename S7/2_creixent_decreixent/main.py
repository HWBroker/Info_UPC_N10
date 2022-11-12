# NoMoreHomework

def main():
    l = int(input())
    x = []
    y = []

    sx = []
    sy = []

    i = 0

    f = True

    while i < l:
        x.append(int(input()))
        y.append(int(input()))
        i += 1
    
    sx = sorted(x)
    sy = sorted(y)
    sy.reverse()

    if sx != x or sy != y:
        f = False

    print(f)

if __name__ == '__main__':
    main()
