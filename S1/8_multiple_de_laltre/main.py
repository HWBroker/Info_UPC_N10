#NoMoreHomework

def main():
    i = int(input())
    j = int(input())

    if i % j == 0 or j % i == 0:
        print('True')
    else:
        print('False')

if __name__ == '__main__':
    main()
