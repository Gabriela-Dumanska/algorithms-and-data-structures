#Euler cycle is a path that visits every edge one time and starts and ends on the same vertex
def Euler_cycle(G):
    Result=[]
    def dfs_visit(G,u):
        for v in range (len(G)):
            if G[u][v]==1:
                G[u][v]=0
                G[v][u]=0
                dfs_visit(G,v)
                Result.append(v)
    for u in range(len(G)):
        dfs_visit(G,u)
    Result.reverse()
    Result.append(Result[0])
    return Result

G=[[0,1,1,0,0,0,0],
   [1,0,0,1,1,0,1],
   [1,0,0,1,1,0,1],
   [0,1,1,0,1,1,0],
   [0,1,1,1,0,1,0],
   [0,0,0,1,1,0,0],
   [0,1,1,0,0,0,0]]

print(Euler_cycle(G))