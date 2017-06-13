from sys import stdin


def main():
    cases = int(stdin.readline())
    while cases > 0:
        grid = stdin.readline().split()
        print((int(grid[0]) // 3) * (int(grid[1]) // 3))
        cases -= 1


main()
