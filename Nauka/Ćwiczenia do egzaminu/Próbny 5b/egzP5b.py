from egzP5btesty import runtests 
from math import inf
#rusunięcie punktu artykulacji powoduje rozspójnienie grafu
#O(2V+E)

def articulation_points(G):
    Result=[False]*len(G)
    R=0
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

    for u in range(len(G)):
        if time[u]<=low[u] and parent[u]!=None and not Result[parent[u]]:
            R+=1
            Result[parent[u]]=True
    return R


def koleje ( B ):
    G=[[] for _ in range (len(B))]
    for i in range(len(B)):
        G[B[i][0]].append(B[i][1])
        G[B[i][1]].append(B[i][0])
    return articulation_points(G)

runtests ( koleje, all_tests=True )

B=[(2, 0), (0, 1), (0, 1), (4, 1), (2, 0), (3, 0), (1, 4), (1, 4), (3, 0), (0, 1), (3, 0), (0, 2), (3, 0), (1, 0), (1, 0), (0, 2), (3, 0)]
#print(koleje(B))