#O(V^2)
def DFS(G):
    visited=[False  for _ in range(len(G))]
    time=[0 for _ in range(len(G))]
    parent=[None for _ in range (len(G))]
    t=0
    def dfs_visit(u):
        nonlocal t
        visited[u]=True
        for v in range (len(G)):
            if not visited[v] and G[u][v]!=0:
                parent[v]=u
                dfs_visit(v)
        time[u]=t
        t+=1
    
    for u in range(len(G)):
        if not visited[u]:
            dfs_visit(u)

    return time, parent

G=      [[0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

print(DFS(G))
