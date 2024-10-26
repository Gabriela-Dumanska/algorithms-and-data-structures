from collections import deque
from math import inf
#najkrótsza ścieżka w grafie nieważonym, smol wierzchołki
def BFS_shortest_path(G,root):
    visited=[False]*len(G)
    distance=[inf]*len(G)
    Q=deque()
    visited[root]=True
    distance[root]=0
    Q.append(root)
    while len(Q):
        u=Q.popleft()
        for v in G[u]:
            if not visited[v]:
                distance[v]=distance[u]+1
                visited[v]=True
                Q.append(v)
    return distance

G = [[1,2],[2,0,6],[0,1],[4,5],[3,5],[3,4],[7],[]]

Result= BFS_shortest_path(G,0)
print(Result)
