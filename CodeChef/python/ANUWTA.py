from sys import stdin


def main():
  cases = int(stdin.readline().strip())
  for _ in range(cases):
    n = int(stdin.readline().strip())
    print((n * (n + 3)) // 2)

main()
