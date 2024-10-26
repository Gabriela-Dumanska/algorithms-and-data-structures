#graf skierowany
def Hamilton_path(G):
    Result=[]
    visited=[False]*len(G)

    def Topological_sorting(G):
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
    Result=Topological_sorting(G)

    for i in range(len(G)-1):
        u=Result[i]
        v=Result[i+1]
        if not v in G[u]:
            return None
    return Result
    
G = [[1,2],[6,3,4],[3,4],[4,5],[5],[],[2]]

Result= Hamilton_path(G)
print(Result)