def Kruskal_MST(G):
    Unions=[i for i in range (len(G))]
    E=[]
    def Find(u):
        if u!=Unions[u]:
            Unions[u]=Find(Unions[u])
        return Unions[u]
    
    def Union(u,v):
        u=Find(u)
        v=Find(v)
        if u==v:
            return False
        Unions[u]=v
        return True
    
    def Edges():
        for u in range(len (G)):
            for v in range (len(G)):
                if G[u][v]!=0:
                    E.append((u,v,G[u][v]))
    
    Edges()
    E.sort(key=lambda x: x[2])
    MST=[]
    for i in range(len(E)):
        u=E[i][0]
        v=E[i][1]
        if Union(u,v):
            MST.append(E[i])

    return MST

G=[[0,7,8,3,2,0],
   [7,0,1,0,0,0],
   [8,1,0,12,0,4],
   [3,0,12,0,0,6],
   [2,0,0,0,0,5],
   [0,0,4,6,5,0]]

print(Kruskal_MST(G))
