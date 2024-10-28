#przeszukiwanie grafu wgłąb z zapisaniem czasu wyjścia z wierzchołka
#O(V+E)
def DFS(G):
    time=[0]*len(G)
    t=0
    visited=[False]*len(G)
    def dfs_visit(G,u):
        nonlocal t
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G,v)
        time[u]=t
        t+=1
        
    for u in range(len(G)):
        if not visited[u]:
            dfs_visit(G,u)
    return time

print(DFS([[1,4],[2,3],[0,7],[4],[5],[3,6],[3],[8],[9],[10],[6,7]]))