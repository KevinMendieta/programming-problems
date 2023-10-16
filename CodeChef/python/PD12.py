from sys import stdin

DELTAS = [
  [0, 1],
  [0, -1],
  [-1, 0],
  [1, 0],
  [-1, 1],
  [1, -1],
  [-1, -1],
  [1, 1]
]

def DFS(graph, i, j, rows, columns):
  global DELTAS
  graph[i][j] = '.'
  for delta in DELTAS:
    new_i = i + delta[0]
    new_j = j + delta[1]

    if (new_i < rows and new_j < columns and new_i >= 0 and new_j >= 0):
      if graph[new_i][new_j] == "#":
        DFS(graph, new_i, new_j, rows, columns) 


def solve(atlas, rows, columns):
  islands_count = 0
  for i in range(rows):
    for j in range(columns):
      if atlas[i][j] == "#":
        DFS(atlas, i, j, rows, columns)
        islands_count += 1
  return islands_count


def main():
  cases = int(stdin.readline().strip())
  for _ in range(cases):
    [rows, columns] = [int(x) for x in stdin.readline().strip().split()]
    atlas = []
    for _ in range(rows):
      atlas.append(list(stdin.readline().strip()))
    print(solve(atlas, rows, columns))


main()
