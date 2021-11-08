from sys import stdin

def DFS(graph, source):
  visited = [False for x in range (len(graph))]
  stack = []
  stack.append(source)
  visited[source] = True
  order = {}
  order[source] = 0
  count = 0
  while stack:
      node = stack.pop()
      count += order[node]
      for i in graph[node]:
          if not(visited[i]):       
              order[i] = order[node] + 1
              stack.append(i)
              visited[i] = True
  return count


def solve(graph):
  string = ""
  for i in range(len(graph)):
    value = DFS(graph, i)
    if (i == len(graph) - 1):
      string += str(value)
    else:
      string += str(value) + " "
  return string

def main():
  n = int(stdin.readline().strip())
  graph = [[] for x in range(n)]
  for i in range(n - 1):
    [u, v] = [int(x) for x in stdin.readline().strip().split(" ")]
    graph[u].append(v)
    graph[v].append(u)
  print(solve(graph))

main()
