#NoMoreHomework

def main():
    i = int(input())
    
    h = int(i / 3600)
    m = int((i - h * 3600) / 60)
    s = int(((i - h * 3600) - (m * 60)))

    print(f"{h} {m} {s}")

if __name__ == '__main__':
    main()
