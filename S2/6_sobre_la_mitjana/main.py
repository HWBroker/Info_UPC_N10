#NoMoreHomework

def main():
    i = [int(input()), int(input()), int(input()), int(input())]
    j = sum(i) / len(i)
    k = []

    for l in i:
        if l > j:
            k.append(i)

    print(len(k))


if __name__ == '__main__':
    main()
