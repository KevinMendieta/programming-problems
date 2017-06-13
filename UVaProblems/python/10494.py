from sys import stdin

def main():
    info = stdin.readline().split()
    while info:
        ans = 0
        if info[1] == '/':
            ans = int(info[0])//int(info[2])
        elif info[1] == '%':
            ans = int(info[0])%int(info[2])
        print(ans)
        info = stdin.readline().split()
main()
