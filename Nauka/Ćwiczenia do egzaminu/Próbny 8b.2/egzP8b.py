from egzP8btesty import runtests
from math import inf

def Floyd_Warshall(G,start,end):
    n=len(G)
    parent=[[None for _ in range (n)] for _ in range (n)]
    distance=[[inf for _ in range (n)] for _ in range (n)]

    for u in range(n):
        for v in range(n):
            if u==v:
                distance[u][v]=0
            elif G[u][v]!=0:
                distance[u][v]=G[u][v]
                parent[u][v]=u
                
    for t in range(n):
        for x in range(n):
            for y in range(n):
                if distance[x][y]>distance[x][t]+distance[t][y]:
                    distance[x][y]=distance[x][t]+distance[t][y]
                    parent[x][y]=parent[t][y]
    while end!=None:
        end=parent[start][end]
    
    return distance


def robot( G, P ):
    NG=[[0 for _ in range(len(G))] for _ in range(len(G))]
    for u in range(len(G)):
        for v in G[u]:
            NG[u][v[0]]=v[1]
            NG[v[0]][u]=v[1]
   
    distance=Floyd_Warshall(NG,0,len(G)-1)
    Result=0
    for i in range(len(P)-1):
        Result+=distance[P[i]][P[i+1]]
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
