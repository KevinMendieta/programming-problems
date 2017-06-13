from sys import stdin
import math

def main():
    size = int(stdin.readline())
    case = 1
    while size != 0:
        bricks = [int(x) for x in stdin.readline().split()]
        total = 0
        moves = 0
        for i in bricks:
            total += i
        total = math.ceil(total/len(bricks))
        for i in bricks:
            if i < total:
                moves += total-i
        print("Set #"+str(case))
        print("The minimum number of moves is "+str(moves)+".")
        print()
        size = int(stdin.readline())
        case += 1
main()
