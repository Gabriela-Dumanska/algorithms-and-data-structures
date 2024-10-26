from math import inf
#najkrótsza ścieżka między każdym a każdym
#O(V^3)
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


G     = [[0, 7, 6, 0, 0, 0, 0, 0, 0],
         [7, 0, 0, 3, 2, 0, 0, 0, 0],
         [6, 0, 0, 0, 0, 2, 0, 0, 0],
         [0, 3, 0, 0, 0, 0, 0, 4, 0],
         [0, 2, 0, 0, 0, 0, 1, 0, 15],
         [0, 0, 2, 0, 0, 0, 3, 4, 0],
         [0, 0, 0, 0, 1, 3, 0, 6, 0],
         [0, 0, 0, 4, 0, 4, 6, 0, -5],
         [0, 0, 0, 0, 15, 0, 0, 5, 0]]

Floyd_Warshall(G,0,8)