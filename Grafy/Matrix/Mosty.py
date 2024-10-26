from math import inf
#most to krawędź, której usunięcie powoduje rozspójnienie grafu
#O(2V+E)

def bridges(G):
    Result=[]
    visited=[False]*len(G)
    time=[0]*len(G)
    low=[inf]*len(G)
    parent=[None]*len(G)
    t=0
    def dfs_visit(G,u):
        nonlocal t
        visited[u]=True
        time[u]=t
        low[u]=t
        t+=1
        for v in range(len(G)):
            if not visited[v] and G[u][v]!=0:
                parent[v]=u
                dfs_visit(G,v)
                low[u]=min(low[u],low[v])
            elif parent[u]!=v and G[u][v]!=0:
                low[u]=min(low[u],time[v])

    for u in range(len(G)):
        if not visited[u]:
            dfs_visit(G,u)
            
    for u in range(len(G)):
        if time[u]==low[u] and parent[u]!=None:
            Result.append((parent[u],u))
    return Result

G=      [[0, 1, 0, 1, 1, 0],
         [1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 0],
         [1, 0, 1, 1, 0, 0],
         [0, 0, 1, 0, 0, 0]]

print(bridges(G))
