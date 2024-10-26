#graf skierowany
def Hamilton_path(G):
    Result=[]
    visited=[False]*len(G)

    def Topological_sorting(G):
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
    Result=Topological_sorting(G)
    print(Result)
    for i in range(len(G)-1):
        u=Result[i]
        v=Result[i+1]
        print(u,v)
        if G[u][v]==0:
            return None
    return Result
    

G=[[0,1,1,0,0,0,0],
   [0,0,0,1,1,0,1],
   [0,0,0,1,1,0,0],
   [0,0,0,0,1,1,0],
   [0,0,0,0,0,1,0],
   [0,0,0,0,0,0,0],
   [0,0,1,0,0,0,0]]

Result= Hamilton_path(G)
print(Result)