from sys import stdin

def main():
    cases = int(stdin.readline())
    while cases:
        a,b,c = [int(x) for x in stdin.readline().split()]
        total = 0; bottles = a+b
        while bottles>=c:
            total += bottles//c
            bottles = bottles//c + bottles%c
        print(total)
        cases -= 1
main()
