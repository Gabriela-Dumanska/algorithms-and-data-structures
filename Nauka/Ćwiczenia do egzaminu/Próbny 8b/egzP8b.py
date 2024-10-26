from egzP8btesty import runtests
from queue import PriorityQueue
from math import inf 

def relax(u,v,distance,parent):
    if distance[v[0]]>distance[u]+v[1]:
        distance[v[0]]=distance[u]+v[1]
        parent[v[0]]=u
        return True
    return False

def Dijkstra(G, source, m):
    q=PriorityQueue()
    q.put((0, source))
    parent = [None] * len(G)
    distance = [inf] * len(G)
    visited = [False] * len(G)
    distance[source] = 0
    while not q.empty():
        d,u=q.get()
        for v in G[u]:
            if not visited[v[0]] and relax(u,v,distance,parent):
                q.put((distance[v[0]],v[0]))
        if u==m:
            return distance[m]
        visited[u]=True

def robot( G, P ):
    Result=0
    for i in range(len(P)-1):
        Result+=Dijkstra(G,P[i],P[i+1])
    return Result
    
runtests(robot, all_tests = True)
G = [
 [(1, 3), (2, 3)],
 [(0, 3), (4, 4)],
 [(0, 3), (3, 1), (4, 4)],
 [(2, 1), (4, 2)],
 [(1, 4), (2, 4), (3, 2)]
]
P = [0, 3, 4]
#print(robot(G,P))
