def BFS(graph, source):
    """An implementation of BFS using a qeu and a integer array O(v+e)
       where v are the vertex and r are the edges Kevin Mendieta Perez 19/02/2016"""
    visited = [0 for x in range(len(graph))]
    qeu, order = [], []
    qeu.append(source)
    visited[source] = 1
    order.append(source)
    while qeu:
        node = qeu.pop(0)
        for i in graph[node]:
            if visited[i] == 0:
                visited[i] = 1
                order.append(i)
                qeu.append(i)
        visited[node] = 2
    print(visited)
    return(order)


print(BFS([[1, 2], [3], [4], [], []], 1))
