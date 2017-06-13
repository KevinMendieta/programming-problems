from sys import stdin

def main():
    cases = int(stdin.readline())
    while cases>0:
        squence = stdin.readline().strip()
        multiplier = 1
        score = 0
        for i in squence:
            if(i=="O"):
                score += 1*multiplier
                multiplier += 1
            else:
                multiplier = 1
        print(score)
        cases -= 1
main()
