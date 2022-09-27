#NoMoreHomework

def main():
    i = {}

    j = [input(), input(), input()]
    k = 0
    l = 0

    for w in j:
        k = i.get(w, 0)
        i[w] = k + 1

    for n in i.values():
        if n > l:
            l = n

    print(l)


if __name__ == "__main__":
    main()
