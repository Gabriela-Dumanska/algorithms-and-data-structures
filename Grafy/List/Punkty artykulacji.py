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
        if time[u]<=low[u] and parent[u]!=None:
            Result.append(parent[u])
    return Result

G=[[1,3,4],[0,3],[4],[0,1,4],[3,0,2]]
H=[[1,2,3],[0,4],[0],[0],[1]]
print(articulation_points(G))
