from sys import stdin

def main():
    cases = int(stdin.readline())
    for i in range (cases):
        speeds = [int(x) for x in stdin.readline().split()]
        leng = speeds.pop(0)
        maxi = 0
        for j in range (leng):
            if speeds[j] > maxi:
                maxi = speeds[j]
        print("Case",str(i+1)+":",maxi)
main()
