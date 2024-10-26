'''
GABRIELA DUMAŃSKA

Na początku funkcja spacetravel oznacza w tablicy O, które wierzchołki są osobliwościami. Następnie przygotowuje Graf w postaci tablicy 
sąsiedztwa uzupełnioną o czas przelotu. Osobliwości traktujemy jako jeden wierzchołek. Następnie przeprowadzamy Algorytm Dijkstry:

Przechowujemy tablicę czasu od a do każdego wierzchołka. Przemieszczamy się po grafie za pomocą BFS uwzględniając na kolejce priotytet czasowy krawędzi.
Aktualizujemy tablicę czasu, gdy nowa trasa, z której przyszliśmy do wierzchołka ma krótszy czas. 

Złożoność tego algorytmu to O(ElogV+E+S).
'''

from zad5testy import runtests
from queue import PriorityQueue
from math import inf


def spacetravel( n, E, S, a, b ):
    G=[[] for _ in range (n+1)]
    O=[False]*n
    for i in range(len(S)):
        O[S[i]]=True
    if  O[a]==True:
        a=n
    if O[b]==True:
        b=n
    for i in range(len(E)):
        if O[E[i][0]]==True:
            G[n].append((E[i][1],E[i][2]))
            G[E[i][1]].append((n,E[i][2]))
        elif O[E[i][1]]==True:
            G[n].append((E[i][0],E[i][2]))
            G[E[i][0]].append((n,E[i][2]))
        else:
            G[E[i][0]].append((E[i][1],E[i][2]))
            G[E[i][1]].append((E[i][0],E[i][2]))    

    q=PriorityQueue()
    visited=[False]*len(G)
    q.put((0,a))
    time=[inf]*len(G)
    time[a]=0
    while not q.empty():
        d,u=q.get()
        for v in G[u]:
                if not visited[v[0]] and time[v[0]]>(time[u]+v[1]):
                    time[v[0]]=time[u]+v[1]
                    q.put((time[v[0]],v[0]))
        visited[u]=True
    if time[b]==inf:
         return None
    return time[b]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )