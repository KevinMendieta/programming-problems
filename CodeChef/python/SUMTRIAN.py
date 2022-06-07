from sys import stdin


def recursive_BP(triangle, size, row, column):
  value = triangle[row][column]
  if (row == size - 1):
    return value
  else:
    return max(
      value + recursive_BP(triangle, size, row + 1, column),
      value + recursive_BP(triangle, size, row + 1, column + 1)
    )


def bottom_up_BP(triangle, size):
  if size == 1:
    return triangle[0][0]

  for i in range(size - 2, -1, -1):
    for j in range(i + 1):
      value = triangle[i][j]
      triangle[i][j] = value + max(
        triangle[i + 1][j],
        triangle[i + 1][j + 1]
      )

  return triangle[0][0]


def solve(triangle, size):
  # recursive:
  # return recursive_BP(triangle, size, 0, 0)
  # bottom up:
  return bottom_up_BP(triangle, size)


def main():
  cases = int(stdin.readline().strip())
  for i in range(cases):
    size = int(stdin.readline().strip())
    triangle = []
    for j in range(size):
      row = [int(x) for x in stdin.readline().strip().split(" ")]
      triangle.append(row)
    print(solve(triangle, size))


main()
