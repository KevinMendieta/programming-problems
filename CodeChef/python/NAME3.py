from sys import stdin


def subs(first, second):
  i, j = 0, 0
  while i < len(first) and j < len(second):
    if first[i] == second[j]:
      i += 1
      j += 1
    else:
      j += 1
  return i == len(first)

def main():
  cases = int(stdin.readline().strip())
  for _ in range(cases):
    first, second = stdin.readline().strip().split()
    is_subs = subs(first, second) if len(first) <= len(second) else subs(second, first)
    if is_subs:
      print("YES")
    else:
      print("NO")


main()
