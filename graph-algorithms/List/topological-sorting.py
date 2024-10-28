#graf skierowany
#każdy wierzchołek w liście wynikowej poprzedza te wierzchołki, do których ma krawędzie
#O(V+E)
def Topological_sorting(G):
    visited=[False]*len(G)
    sort=[]
    def dfs_visit(G,u):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G,v)
        sort.append(u)
    for u in range(len(G)):
        if not visited[u]:
            dfs_visit(G,u)
    sort.reverse()
    return sort

G = [[],[2,3],[4],[4],[5],[6],[]]

Result=Topological_sorting(G)
print(Result)