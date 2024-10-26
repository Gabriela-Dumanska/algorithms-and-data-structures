from queue import PriorityQueue
from math import inf 
#finding minimal spanning tree- a tree that contains every vertex, but the edges are minimal
#O(ElogV)
def Prim(G,source):
    n=len(G)
    Q=PriorityQueue()
    parent=[None for _ in range (n)]
    distance=[inf for _ in range(n)]
    visited=[False for _ in range(n)]
    visited[source]=True
    distance[source]=0
    Q.put((0,source))
    while not Q.empty():
        d,u=Q.get()
        visited[u]=True
        for v,w in G[u]:
            if distance[v]>w and not visited[v]:
                parent[v]=u
                distance[v]=w
                Q.put((w,v))
    MST=[]
    for i in range (n):
        if parent[i] is not None:
            MST.append((i,parent[i], distance[i]))
    return MST
    
G =     [[(1, 7), (2, 8), (3, 3), (4, 2)],
         [(0, 7), (2, 1)],
         [(0, 8), (1, 1), (3, 12), (5, 4)],
         [(0, 3), (2, 12), (5, 6)],
         [(0, 2), (5, 5)],
         [(2, 4), (3, 6), (4, 5)]]

print(Prim(G,0))
