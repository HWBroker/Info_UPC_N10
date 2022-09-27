#NoMoreHomework

def main():
    i = input()

    j = int(i[0])
    k = int(i[1])
    l = int(i[2])

    if (j + k + l) % 5 == 0:
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()
