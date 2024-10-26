from queue import PriorityQueue
from math import inf 
#najkrótsza ścieżka od źródła do wszystkich innych w grafie ważonym o wagach dodatnich
#O(V^2)
def relax(u,v,distance,parent):
    if distance[v]>distance[u]+G[u][v]:
        distance[v]=distance[u]+G[u][v]
        parent[v]=u
        return True
    return False

def Dijkstra(G, source):
    q=PriorityQueue()
    q.put((0, source))
    parent = [None] * len(G)
    distance = [inf] * len(G)
    visited = [False] * len(G)
    distance[source] = 0
    while not q.empty():
        d,u=q.get()
        for v in range(len(G)):
            if G[u][v]!=0 and not visited[v] and relax(u,v,distance,parent):
                q.put((distance[v],v))
        visited[u]=True
    return distance

G=[[0,7,8,3,2,0],
   [7,0,1,0,0,0],
   [8,1,0,1,0,1],
   [3,0,1,0,0,6],
   [2,0,0,0,0,5],
   [0,0,1,6,5,0]]

print(Dijkstra(G,0)) 
