#szukanie najkrótszych ścieżek między źródłem, a każdym innym wierzchołkiem w grafie skierowanym
#z krawędziami o ujemnych wagach
#O(VE)
from math import inf
def relax(distance,parent,edge):
    if distance[edge[1]]>distance[edge[0]]+edge[2]:
        distance[edge[1]]=distance[edge[0]]+edge[2]
        parent[edge[1]]=edge[0]

def Bellman_Ford(G,s):
    E=len(G)
    V=0
    for i in range (E):
        V=max(V,G[i][0], G[i][1])
    parent=[None]*(V+1)
    distance=[inf]*(V+1)
    distance[s]=0
    for i in range (V-1):
        for j in range (E):
            relax(distance,parent,G[j])
    for i in range (E):
        if distance[G[i][1]]>distance[G[i][0]]+G[i][2]:
            return False,[],[] #ujemny cykl
    return True, parent, distance

G=[[0,1,1,],[1,3,2],[2,0,-1],[3,2,-2]]
result,parent,distance=Bellman_Ford(G,0)
if result:
    for i in range (len(parent)):
        print(i,distance[i])
else:
    print("Ujemny cykl!")

            
        

