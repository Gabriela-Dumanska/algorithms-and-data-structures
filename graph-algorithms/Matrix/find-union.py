def Find_Union(G):
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

    for u,v,w in E:
        Union(u,v)
    
    return Unions


G=[[0,1,1,0,0,0,0],
   [0,0,0,1,1,0,1],
   [0,0,0,1,1,0,0],
   [0,0,0,0,1,1,0],
   [0,0,0,0,0,1,0],
   [0,0,0,0,0,0,0],
   [0,0,1,0,0,0,0]]

print(Find_Union(G))
