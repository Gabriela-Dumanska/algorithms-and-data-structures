from egzP3btesty import runtests 
from queue import PriorityQueue
#finding minimal spanning tree- a tree that contains every vertex, but the edges are minimal
#O(ElogV)
def Kruskal_MST(G):
    Unions=[i for i in range (len(G))]
    E=[]
    suma=0

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
        nonlocal suma
        for u in range(len (G)):
            for v, w in G[u]:
                suma+=w
                E.append((u,v,w))
                G[v].remove((u,w))


    Edges() 
    E.sort(key=lambda x: -x[2])
    MST=[]
    x=0
    print(E)
    for i in range(len(E)):
        u=E[i][0]
        v=E[i][1]
        if Union(u,v):
            MST.append(E[i])
            suma-=E[i][2]
        elif x==0:
            x=E[i][2]
    return suma-x



H =     [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]

G = [
[(1, 15), (2, 5), (3, 10) ],
[(0, 15), (2, 8), (4, 5), (5, 12)],
[(0, 5), (1, 8), (3, 5), (4, 6) ],
[(0, 10), (2, 5), (4, 2), (5, 11)],
[(1, 5), (2, 6), (3, 2), (5, 2) ],
[(1, 12), (4, 2), (3, 11) ]
]


def lufthansa ( G ):
    return Kruskal_MST(G)

runtests ( lufthansa, all_tests=True )