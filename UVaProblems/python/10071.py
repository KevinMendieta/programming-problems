from sys import stdin

def main():
    data = [int(x) for x in stdin.readline().split()]
    while data:
        print(2*data[0]*data[1])
        data = [int(x) for x in stdin.readline().split()]
main()
