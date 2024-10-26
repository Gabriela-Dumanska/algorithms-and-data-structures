from kol2testy import runtests
'''
GABRIELA DUMAŃSKA
Należy zauważyć, że piękne drzewo rozpinające musi iść po krawędziach, których wagi są kolejnymi liczbami.
Wykorzystuję algorytm Kruskala, ponieważ szuka on MST idąc po krawędziach o rosnących wagach. Jeśli algorytm chce pominąć, którąś
krawędź- przerywam go i puszczam od kolejnego wierzchołka.

Obstawiam złożoność O(VElog V)
'''
def beautree(G):
    def Kruskal_MST(G):
        Unions=[i for i in range (len(G))]
        E=[]
        def Find(u):
            if u!=Unions[u]:
                Unions[u]=Find(Unions[u])
            return Unions[u]
        
        def Union(u,v):
            u=Find(u)
            v=Find(v)
            if u==v:
                return False
            Unions[u]=v
            return True
        
        def Edges():
            for u in range(len (G)):
                for v, w in G[u]:
                    E.append((u,v,w))
                    G[v].remove((u,w))

        Edges() 
        E.sort(key=lambda x: x[2])
        MST=[]
        for j in range(len(E)):
            visited=[False]*len(G)
            fl=0
            weight=0
            for i in range(j,len(E)):
                u=E[i][0]
                v=E[i][1]
                result=Union(u,v)
                if result:
                    MST.append(E[i])
                    weight+=E[i][2]
                    visited[u]=True
                    visited[v]=True
                else: #algorytm nie dołącza krawędzi do drzewa
                    for q in range((len(G))): #sprawdzam, czy to czasem nie koniec wyznaczania MST
                        if visited[q]==False: #jeśli któryś wierzchołek nie był odwiedzony, rozpoczynam szukanie MST od nowa
                            MST=[]
                            Unions=[i for i in range (len(G))]
                            fl=1
                            break
                    if fl==1: 
                        break
                    else: #jeśli algorytm odwiedził wszystkie wierzchołki- zwracam wagę drzewa
                        return weight
                    
        if len(MST)==0:
            return None
        return weight

    return(Kruskal_MST(G)) 

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )