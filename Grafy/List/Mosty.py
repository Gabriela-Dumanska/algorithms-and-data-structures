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
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                dfs_visit(G,v)
                low[u]=min(low[u],low[v])
            elif parent[u]!=v:
                low[u]=min(low[u],time[v])

    for u in range(len(G)):
        if not visited[u]:
            dfs_visit(G,u)
    print(time, low)
    for u in range(len(G)):
        if time[u]==low[u] and parent[u]:
            Result.append((parent[u],u))
    return Result

G=[[1,3,4],[0,3],[4],[0,1,4],[3,0,2]]
#print(bridges([[1, 4], [0, 2], [1, 3, 4], [2, 5, 6], [0, 2], [3, 6], [3, 5, 7], [6]]))
print(bridges(G))