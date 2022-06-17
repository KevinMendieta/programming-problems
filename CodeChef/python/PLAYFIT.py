from sys import stdin


def solve(A, N):
  max_diff = 0
  min_number = A[0]
  for i in range(1, N):
    max_diff = max(max_diff, A[i] - min_number)
    if (A[i] < min_number):
      min_number = A[i]

  if max_diff > 0:
    return max_diff
  else:
    return "UNFIT"


def main():
  cases = int(stdin.readline().strip())
  for _ in range(cases):
    N = int(stdin.readline().strip())
    matches = [int(x) for x in stdin.readline().strip().split()]
    print(solve(matches, N))


main()
