from sys import stdin

def main():
    cases = int(stdin.readline())
    while cases > 0 :
        num = int(stdin.readline())
        num *= 567
        num /= 9
        num += 7492
        num *= 235
        num /= 47
        num -= 498
        num %= 100
        num //= 10
        print(abs(int(num)))
        cases -=1
main()
