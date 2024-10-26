'''
GABRIELA DUMANSKA

Algorytm wyznacza najtańszą trasę z s do każdego innego wierzchołka za pomocą algorytmu Dijkstry. Następnie przeprowadzamy napad na każdy możliwy zamek.
Znowu liczymy trasę najtańszą trasę, ale z rabowanego zamku do t za pomocą algorytmu Dijsktra_2- mnoży cenę każdej krawędzi razy 2 i dodaje r. 
Wyliczamy na tej podstawie cenę całej trasy= Droga z s do zamku - łup z zamku + Droga będąc ściganym z zamku do t.
Wyznaczamy minimum z każdej iteracji- to nasz wynik.

Złożoność: O(V*ElogV)

'''
from egz1Atesty import runtests
from queue import PriorityQueue
from math import inf 


def relax(u,v,distance):
    if distance[v[0]]>distance[u]+v[1]:
        distance[v[0]]=distance[u]+v[1]
        return True
    return False

def Dijkstra(G, source):
    q=PriorityQueue()
    q.put((0, source))
    distance = [inf] * len(G)
    visited = [False] * len(G)
    distance[source] = 0
    while not q.empty():
        d,u=q.get()
        for v in G[u]:
            if not visited[v[0]] and relax(u,v,distance):
                q.put((distance[v[0]],v[0]))
        visited[u]=True
    return distance

def relax_2(u,v,distance,r):
    if distance[v[0]]>distance[u]+(v[1]*2+r):
        distance[v[0]]=distance[u]+(v[1]*2+r)
        return True
    return False

def Dijkstra_2(G, source, t,r):
    q=PriorityQueue()
    q.put((0, source))
    distance = [inf] * len(G)
    visited = [False] * len(G)
    distance[source] = 0
    while not q.empty():
        d,u=q.get()
        for v in G[u]:
            if not visited[v[0]] and relax_2(u,v,distance,r):
                q.put((distance[v[0]],v[0]))
        if u==t:
            return distance[t]
    return distance[t]
            
        
def gold(G,V,s,t,r):
  distances_from_source=Dijkstra(G,s)
  Result=inf
  for v in range(len(G)):
    path=Dijkstra_2(G,v,t,r)
    robbery=distances_from_source[v]-V[v]+path

    Result=min(robbery,Result)
  return Result

# zmien all_tests na True zeby uruchomic wszystkie testy

runtests( gold, all_tests = True)