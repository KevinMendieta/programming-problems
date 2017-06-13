from sys import stdin

def main():
    bottle = int(stdin.readline())
    while (bottle > 0):
        print(bottle//2)
        bottle = int(stdin.readline())
main()
