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
        for v in range(len(G)):
            if G[u][v]!=0 and distance[v]>G[u][v] and not visited[v]:
                parent[v]=u
                distance[v]=G[u][v]
                Q.put((G[u][v],v))
    MST=[]
    for i in range (n):
        if parent[i] is not None:
            MST.append((i,parent[i], distance[i]))
    return MST
    
G=[[0,7,8,3,2,0],
   [7,0,1,0,0,0],
   [8,1,0,12,0,4],
   [3,0,12,0,0,6],
   [2,0,0,0,0,5],
   [0,0,4,6,5,0]]

print(Prim(G,0))
