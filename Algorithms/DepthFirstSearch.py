def DFS(graph,source):
    """An implementation of DFS using a stack and a boolean array O(v+e)
       where v are the vertex and r are the edges Kevin Mendieta Perez 19/02/2016"""
    visited = [False for x in range (len(graph))]
    out =[]
    stack = []
    stack.append(source)
    visited[source] = True
    while len(stack)>0:
        node = stack.pop()
        out.append(node)
        for i in graph[node]:
            if not(visited[i]):                
                stack.append(i)
                visited[i] = True
    return out
