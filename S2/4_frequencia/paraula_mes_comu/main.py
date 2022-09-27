#NoMoreHomework

def main():
    i = {}

    j = [input(), input(), input()]
    k = 0
    l = 0

    for m in j:
        k = i.get(m, 0)
        i[m] = k + 1

    for n in i.values():
        if n > l:
            l = n

    print(l)


if __name__ == "__main__":
    main()
