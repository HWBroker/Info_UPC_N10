#NoMoreHomework

def main():
    h = int(input()) 
    
    for i in range(1, h + 1):
        w = (i * 2) - 1
        s = (((h * 2) - 1) - w) // 2
        print(f"{' '*s}{'*'*w}")

if __name__ == '__main__':
    main()

