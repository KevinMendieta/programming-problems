from sys import stdin
NUMBERS = [None for x in range(1001)]
def solve():
  global NUMBERS
  NUMBERS[0] = 0
  NUMBERS[1] = 1
  for i in range(2, 1001):
    if (i % 2 == 0):
      NUMBERS[i] = min(NUMBERS[i // 2] + 2, NUMBERS[i - 1] + 1)
    else:
      NUMBERS[i] = NUMBERS[i - 1] + 1

def main():
  global NUMBERS
  cases = int(stdin.readline().strip())
  for i in range(cases):
    n = int(stdin.readline().strip())
    print(NUMBERS[n])

solve()
main()