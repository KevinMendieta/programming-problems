from sys import stdin

def main():
    cases = int(stdin.readline())
    for i in range (cases):
        lon = int(stdin.readline())
        low , hi = 0,0
        walls = [int(x) for x in stdin.readline().split()]
        for j in range (lon-1):
            if walls[j] < walls[j+1]:
                hi += 1
            elif walls[j] > walls[j+1]:
                low += 1
        print("Case "+str(i+1)+": "+str(hi)+" "+str(low))
main()
