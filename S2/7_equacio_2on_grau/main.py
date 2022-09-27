#NoMoreHomework

import math

def eq(a, b, c):
    sq = (pow(b,2)-4*a*c)
    if sq < 0:
        return 'NO'
    if sq == 0:
        return ((-b+(math.sqrt(pow(b, 2)-(4*a*c))))/(2*a))
    else:
        r1 = ((-b+(math.sqrt(pow(b, 2)-(4*a*c))))/(2*a))
        r2 = ((-b-(math.sqrt(pow(b, 2)-(4*a*c))))/(2*a))
        return f"{r1} {r2}"

def main():
    abc = [int(input()), int(input()), int(input())]
    print(eq(abc[0], abc[1], abc[2]))

if __name__ == '__main__':
    main()


