def DFS(G,u):
    stack=[u]
    Result=[]
    visited=[False]*len(G)
    while stack:
        u=stack.pop()
        if visited[u] is False:
            visited[u]=True
            for v in G[u]:
                stack.append(v)
            Result.append(u)
    return Result

G = [[1,2],[2,0],[0,1,4],[4,5],[3,5],[3,4]]

Result= DFS(G,0)
print(Result)