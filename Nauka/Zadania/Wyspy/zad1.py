from zad1testy import runtests
from queue import PriorityQueue
from math import inf 
def islands(G,a,b):

    def relax(u,v,distance,parent):
        if distance[v]>distance[u]+G[u][v]:
            distance[v]=distance[u]+G[u][v]
            parent[v]=u
            return True
        return False

    def Dijkstra(G, source, b):
        q=PriorityQueue()
        q.put((0, source))
        parent = [None] * len(G)
        distance = [inf] * len(G)
        visited = [False] * len(G)
        distance[source] = 0
        prev=0
        while not q.empty():
            d,u=q.get()
            for v in range(len(G)):
                if G[u][v]!=0 and not visited[v] and prev!=G[u][v] and relax(u,v,distance,parent):
                    prev=G[u][v]
                    q.put((distance[v],v))
            visited[u]=True
        return parent
    return Dijkstra(G,a,b)
    

     
G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,100,0 ],
[1,0,0,1,0,0,8 ],
[8,1,1,0,5,0,0 ],
[0,0,0,5,0,0,0 ],
[0,100,0,0,0,0,5 ],
[0,0,8,0,0,5,0 ] ]

print(islands(G1,5,2))

#runtests(islands)