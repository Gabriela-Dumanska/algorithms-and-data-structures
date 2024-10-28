#Maximum flow ~n^4
from collections import deque
from math import inf 

def BFS(G,s,t,parent):
    visited=[False for _ in range(len(G))]
    Q=deque()
    visited[s]=True
    Q.append(s)
    while len(Q):
        u=Q.popleft()
        for v in range (len(G)):
            if not visited[v] and G[u][v]!=0:
                Q.append(v)
                visited[v]=True
                parent[v]=u
    return visited[t]

def edmonds_karp_algorithm(G,s,t):
    parent=[None for _ in range (len(G))]
    max_flow=0
    while BFS(G,s,t,parent):
        flow=inf
        u=t
        while u!=s:
            v=parent[u]
            flow=min(flow,G[v][u])
            u=v
        max_flow+=flow
        u=t
        while u!=s:
            v=parent[u]
            G[v][u]-=flow
            G[u][v]+=flow
            u=v
    return max_flow

graph = [[0, 11, 12, 17, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 14, 0, 0, 0, 0],
         [0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 9, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 7, 0, 10, 0],
         [0, 0, 0, 0, 0, 0, 6, 9, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 8],
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

print(edmonds_karp_algorithm(graph, 0, 9))
