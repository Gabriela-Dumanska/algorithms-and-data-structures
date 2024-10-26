#przeszukiwanie grafu wgłąb
#O(V+E)
def DFS(G):
    visited=[False]*len(G)
    def dfs_visit(G,u):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G,v)
    for u in range(len(G)):
        if not visited[u]:
            dfs_visit(G,u)
    return visited

G = [[1,2],[2,0],[0,1],[4,5],[3,5],[3,4]]

Result= DFS(G)
print(Result)