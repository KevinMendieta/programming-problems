from sys import stdin

def main():
    cases = int(stdin.readline())
    while cases != 0:
        mini, maxi = float("inf"),float("-inf")
        numbers = [x for x in stdin.readline().split()]
        for i in numbers:
            if int(i) > maxi:
                maxi = int(i)
            if int(i) < mini:
                mini = int(i)
        ans = None
        for i in numbers:
            if int(i)!= maxi and int(i)!= mini:
                ans = i
        if ans != None:
            print(ans)
        else:
            print(mini)
        cases -= 1
main()
