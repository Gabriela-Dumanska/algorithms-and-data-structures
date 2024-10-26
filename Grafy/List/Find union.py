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
            for v, w in G[u]:
                E.append((u,v,w))
    
    Edges()

    for u,v,w in E:
        Union(u,v)
    
    return Unions


G =     [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]
print(Find_Union(G))
