#NoMoreHomework

def main():
    for i in range(10, 100):
        j = (i // 10) + (i % 10)
        if (j) < 10:
            print(f"{i}{j}")

if __name__ == '__main__':
    main()
