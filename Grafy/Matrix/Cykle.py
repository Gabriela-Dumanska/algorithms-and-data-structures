def cycle(G):
    visited=[False]*len(G)
    parent=[None]*len(G)
    def dfs_visit(u):
        visited[u]=True
        for v in range(len(G)):
            if G[u][v]==1:
                if not visited[v]:
                    parent[v]=u
                    dfs_visit(v)
                elif parent[u]!=v:
                    return True
    for u in range(len(G)):
        if not visited[u]:
            if dfs_visit(u):
                return True
    return False

G=[[0,1,1,0,0,0,0],
   [1,0,0,1,1,0,1],
   [1,0,0,1,1,0,1],
   [0,1,1,0,1,1,0],
   [0,1,1,1,0,1,0],
   [0,0,0,1,1,0,0],
   [0,1,1,0,0,0,0]]

print(cycle(G))