from egzP1btesty import runtests 
from queue import PriorityQueue
from math import inf 

def relax(u,v,distance,parent, finish):
    if v[0]==finish:
        pom=u
        for i in range (3):
            p=parent[pom]
            if p==None:
                return False
            pom=p
        if p!=0:
            return False
      
    if distance[v[0]]>distance[u]+v[1]:
        distance[v[0]]=distance[u]+v[1]
        parent[v[0]]=u
        return True
    return False

def Dijkstra(G, source, finish):
    q=PriorityQueue()
    q.put((0, source))
    parent = [None] * len(G)
    distance = [inf] * len(G)
    visited = [False] * len(G)
    distance[source] = 0
    while not q.empty():
        d,u=q.get()
        for v in G[u]:
            if not visited[v[0]] and relax(u,v,distance,parent,finish):
                q.put((distance[v[0]],v[0]))
        if(u==finish):
            return distance[finish]

#print(Dijkstra([[(1,9),(2,1)],[(2,2),(0,9),(4,3),(3,8)],[(0,1),(1,2),(4,7),(5,1)],[(1,8),(4,7),(6,8)],[(1,3),(2,7),(5,6),(3,7),(6,1)],[(2,1),(4,6),(6,1)],[(4,1),(3,8),(5,1)]],0, 6)) 

def turysta( G, D, L ):
    V=[[] for _ in range(100000)]
    for i in range(len(G)):
        V[G[i][0]].append((G[i][1],G[i][2]))
        V[G[i][1]].append((G[i][0],G[i][2]))
    return Dijkstra(V,D,L)

runtests ( turysta )
G = [
(0, 1, 9), (0, 2, 1),
(1, 2, 2), (1, 3, 8),
(1, 4, 3), (2, 4, 7),
(2, 5, 1), (3, 4, 7),
(4, 5, 6), (3, 6, 8),
(4, 6, 1), (5, 6, 1)
]
D = 0
L = 6
#print(turysta(G,D,L))