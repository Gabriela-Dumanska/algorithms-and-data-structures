from egzP7atesty import runtests 
#Maximum flow 
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
def akademik( T ):
    n=len(T)
    nnn=0
    G=[[0 for _ in range(2*n+2)] for _ in range(2*n+2)]
    for i in range(n):
        G[2*n][i]=1
        if T[i][0]==None and T[i][1]==None and T[i][2]==None:
            nnn+=1
        else:
            for j in range(3):
                if T[i][j]!=None:
                    G[i][T[i][j]+n]=1
                    G[T[i][j]+n][2*n+1]=1
    proper_rooms=edmonds_karp_algorithm(G,2*n,2*n+1)
    return n-proper_rooms-nnn
T = [(2, 3, None), (0, 1, 3), (0, 2, None), (1, 3, 4), (2, 3, None)]
#print(akademik(T))
runtests ( akademik )