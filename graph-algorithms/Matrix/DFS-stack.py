def DFS(G,u):
    stack=[u]
    Result=[]
    visited=[False]*len(G)
    while stack:
        u=stack.pop()
        if visited[u] is False:
            visited[u]=True
            for v in range(len(G[u])):
                if not visited[v] and G[u][v]!=0:
                 stack.append(v)
            Result.append(u)
    return Result

G=      [[0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

Result= DFS(G,0)
print(Result)