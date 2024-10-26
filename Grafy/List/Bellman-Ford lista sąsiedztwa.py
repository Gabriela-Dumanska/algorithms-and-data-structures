#szukanie najkrótszych ścieżek między źródłem, a każdym innym wierzchołkiem w grafie skierowanym
#z krawędziami o ujemnych wagach
#O(VE)
from math import inf
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
              return False,[],[] #ujemny cykl
    return True, parent, distance

#G=[[(1,-1),(2,4)],[(2,3),(4,2),(3,2)],[],[(2,5),(1,1)],[(3,-3)]]
G=[[(1,1)],[(3,2)],[(0,-1)],[(2,-3)]] #cykl ujemny
result,parent,distance=Bellman_Ford(G,0)
if result:
    for i in range (len(parent)):
        print(i,distance[i])
else:
    print("Ujemny cykl!")

            
        

