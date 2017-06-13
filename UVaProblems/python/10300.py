from sys import stdin
def main():
    cases = int(stdin.readline())
    while cases > 0:
        numberFarmers = int(stdin.readline())
        premiun = 0
        for i in range (numberFarmers):
            info = [int(x) for x in stdin.readline().split()]
            premiun += info[0]*info[2]
        print(premiun)
        cases -= 1
main()
