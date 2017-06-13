from sys import stdin

def main():
    numbers = [int(x) for x in stdin.readline().split()]
    while numbers:
        ans = numbers[1]-numbers[0]
        if ans < 0 :
            print(ans*-1)
        else:
            print(ans)
        numbers = [int(x) for x in stdin.readline().split()]
main()
