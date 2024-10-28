from queue import PriorityQueue
from math import inf 
#najkrótsza ścieżka od źródła do wszystkich innych w grafie ważonym o wagach dodatnich
#O(ElogV)
def relax(u,v,distance,parent):
    if distance[v[0]]>distance[u]+v[1]:
        distance[v[0]]=distance[u]+v[1]
        parent[v[0]]=u
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
        print("u=",u)
        for v in G[u]:
            print("v=",v[0])
            if not visited[v[0]] and relax(u,v,distance,parent):
                q.put((distance[v[0]],v[0]))
            print(distance)
        visited[u]=True
    return distance

print(Dijkstra([[(1,1),(2,4),(3,2)],[(2,0),(3,21)],[(3,0)],[]],0)) 
