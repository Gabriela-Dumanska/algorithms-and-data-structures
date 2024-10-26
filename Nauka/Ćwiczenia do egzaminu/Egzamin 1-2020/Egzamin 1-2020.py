from zad1testy import runtests
from queue import PriorityQueue
from math import inf 
def relax(u,v,distance,parent):
    if parent[u]:
        if G[parent[u]][u]==G[u][v]:
            return False
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
def Islands(G,a,b):
    distance=(Dijkstra(G,a))
    return distance[b]
    
#najkrótsza ścieżka od źródła do wszystkich innych w grafie ważonym o wagach dodatnich
#O(V^2)


G = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,5,0 ],
[0,8,0,0,5,0,5 ],
[0,0,8,1,0,5,0 ] ]


#print(Islands(G,5,2)) 

runtests(Islands)