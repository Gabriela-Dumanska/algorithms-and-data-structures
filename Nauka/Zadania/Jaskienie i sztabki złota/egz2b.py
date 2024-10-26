from egz2btesty import runtests
from math import inf

def magic( C ):

    def relax(distance,parent,edge):
        if distance[edge[1]]>distance[edge[0]]+edge[2]:
            distance[edge[1]]=distance[edge[0]]+edge[2]
            parent[edge[1]]=edge[0]

    def Bellman_Ford(G,s):
        V=len(G)
        parent=[None]*V
        distance=[inf]*V
        distance[s]=0
        for i in range (V-1):
            for j in range (V):
                for q in range (len(G[j])):
                    relax(distance,parent,(j,G[j][q][0],G[j][q][1]))
        for i in range (V):
            for j in range (len(G[i])):
                if distance[G[i][j][0]]>distance[i]+G[i][j][1]:
                    return False,[] #ujemny cykl
        return True, distance
    
    G=[[] for _ in range (len(C))]
    for i in range (len(C)):
        for j in range(1,len(C[i])):
            if C[i][j][1]!=-1:
                if C[i][j][0]<=C[i][j][1]+10:
                    G[i].append((C[i][j][1],C[i][j][0]-C[i][0]))
    result,distance=Bellman_Ford(G,0)
    print(C)
    if result:
        return -(distance[len(G)-1])
    return False


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = False )
#C = [ [8, [ 6, 3], [ 4, 2], [7, 1]], # 0
#[22, [12, 2], [21, 3], [0,-1]], # 1
#[9, [11, 3], [ 0,-1], [7,-1]], # 2
#[15, [ 0,-1], [ 1,-1], [0,-1]] ] # 3
#print(magic(C))