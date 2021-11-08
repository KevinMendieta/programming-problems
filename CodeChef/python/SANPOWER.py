from sys import stdin
MEMO = []

def power(arr, k, turn):
  max = arr[0]
  for i in range(len(arr)):
    if arr[i] > max:
      max = arr[i]
  res = k * turn + max
  return res

def memo_solve(arr, i, j, turn):
  global MEMO
  if (MEMO[i][j]):
    return MEMO[i][j]
  if (i == j):
    MEMO[i][j] = arr[i] * turn + arr[i]
    return MEMO[i][j]
  else:
    MEMO[i][j] = max(
      memo_solve(arr, i + 1, j, turn + 1) + power(arr, arr[i], turn),
      memo_solve(arr, i, j - 1, turn + 1) + power(arr, arr[j], turn)
    )
    return MEMO[i][j]

def main():
  global MEMO
  n = int(stdin.readline().strip())
  arr = [int(x) for x in stdin.readline().strip().split(" ")]
  for i in range(n):
    MEMO.append([None for x in range(n)])
  print(memo_solve(arr, 0, 0 if n == 0 else n - 1, 1))

main()
