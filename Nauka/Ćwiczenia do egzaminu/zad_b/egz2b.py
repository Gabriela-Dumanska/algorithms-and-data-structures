from egz2btesty import runtests
from math import inf

def relax(u,v,distance):
    if u[2]>10:
        chamber=distance[u[1]]+10
        if u[2]-10<v[1]:
            chamber-=(v[1]-u[2]+10)
            if chamber<0: return False
    else:
        chamber=distance[u[1]]+u[2]
        chamber-=v[1]
        if chamber<0: return False
    print(distance[u[1]],u[2],v[1],chamber)
    if distance[v[0]]<chamber:
        distance[v[0]]=chamber
        return True
    return False


def relax(distance,u,v,cost,gold):
    if gold>10:
        chamber=distance[u]+10
        if gold-10<cost:
            chamber-=(cost-gold+10)
    else:
        chamber=distance[u]+gold
        chamber-=cost
    if chamber<0: return
    if distance[v]<chamber:
        distance[v]=chamber

def Bellman_Ford(G,start, C):
    V=len(G)
    distance=[-inf]*V
    distance[start]=0
    for i in range (V-1):
        for j in range (V):
            for q in range (len(G[j])):
                relax(distance,j,G[j][q][0],G[j][q][1],G[j][q][2])
    return distance

def magic( C ):
    G=[[] for _ in range (len(C))]
    for i in range(len(C)):
        for j in range(1,len(C[i])):
            if C[i][j][1]!=-1:
                G[i].append((C[i][j][1],C[i][j][0],C[i][0]))
    return Bellman_Ford(G,0,C)[len(C)-1]
    
  

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
C = [ [8, [ 6, 3], [ 4, 2], [7, 1]], # 0
[22, [12, 2], [21, 3], [0,-1]], # 1
[9, [11, 3], [ 0,-1], [7,-1]], # 2
[15, [ 0,-1], [ 1,-1], [0,-1]] ] # 3
H=[[2, [5, 1], [1, 6], [1, 8]],
[2, [7, 2], [1, 4], [1, 2]],
[89, [91, 3], [75, 8], [84, 6]],
[8, [6, 4], [10, 6], [7, 5]],
[4, [5, 5], [1, 7], [3, 5]],
[10, [11, 6], [0, 6], [4, 6]],
[1, [0, 7], [0, 7], [6, 7]],
[57, [51, 8], [45, 8], [50, 8]],
[2, [6, 9], [7, 9], [0, 9]],
[6, [3, -1], [8, -1], [1, -1]]]
#magic(H)
 