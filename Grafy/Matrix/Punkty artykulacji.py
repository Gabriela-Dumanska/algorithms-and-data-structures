from math import inf
#rusunięcie punktu artykulacji powoduje rozspójnienie grafu
#O(2V+E)

def articulation_points(G):
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

    print(time, low)
    for u in range(len(G)):
        print(u, time[u],low[u],parent[u])
        if time[u]<=low[u] and parent[u]!=None:
            Result.append(parent[u])
    return Result

G=      [[0, 1, 0, 1, 1, 0],
         [1, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 1],
         [1, 1, 0, 0, 1, 0],
         [1, 0, 1, 1, 0, 0],
         [0, 0, 1, 0, 0, 0]]
print(articulation_points(G))
