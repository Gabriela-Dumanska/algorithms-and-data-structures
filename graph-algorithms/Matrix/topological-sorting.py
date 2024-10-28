#graf skierowany
#każdy wierzchołek w liście wynikowej poprzedza te wierzchołki, do których ma krawędzie
#O(V^2)
def Topological_sorting(G):
    visited=[False  for _ in range(len(G))] 
    sort=[]
    def dfs_visit(u):
        visited[u]=True
        for v in range (len(G)):
            if not visited[v] and G[u][v]!=0:
                dfs_visit(v)
        sort.append(u)
    for u in range(len(G)):
        if not visited[u]:
            dfs_visit(u)
    sort.reverse()
    return sort

G=      [[0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 1, 0, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 0, 0, 0, 0, 0, 0]]

print(Topological_sorting(G))