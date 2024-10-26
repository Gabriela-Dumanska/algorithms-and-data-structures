'''
GABRIELA DUMAŃSKA

Algorytm znajduje najkrótszą ścieżkę w grafie za pomocą algorytmu BFS. Usuwamy jedną krawędź- t, rodzic t.
Ponownie uruchamiamy BFS. Jeśli ścieżka się wydłużyła, to zwracamy usuniętą krawędź. Jeśli ścieżka pozostała 
najkrótsza, przesuwamy się w stronę s- usuwamy krawędź rodzic(rodzic t), rodzic t. Gdy dojdziemy z usuwaniem
aż do źródła, a ścieżka nadal się nie wydłużyła, zwracamy None, ponieważ najkrótszych ścieżek istnieje wiele.

Obstawiam złożoność pesymistyczną O(E*(V+E)), gdzie V to liczba wierzchołków, E krawędzi. W najlepszym
przypadku to rząd O(V+E).
'''

from zad4testy import runtests
from collections import deque

def longer( G, s, t ):
    P=1000000
    def BFS(G,r):
        d=[1000000]*len(G)
        p=[-1]*len(G)
        q=deque()
        visited=[False]*len(G)
        q.append(r)
        visited[r]=True
        d[r]=0
        while len(q):
            u=q.popleft()
            for v in G[u]:
                if not visited[v]:
                    q.append(v)
                    visited[v]=True
                    d[v]=d[u]+1
                    p[v]=u

                    if v==t:
                        return True,p,d
        return False,p,d
    path,p,d=BFS(G,s)
    if path==False:
        return None
    P=d[t]
    a=p[t]
    b=t
    g=G
    if a==s:
        return a,b
    g[a].remove(b)
    g[b].remove(a)
    while P==d[t]:
        path,p,d=BFS(G,s)
        if path==False:
         return (a,b)
        if p[a]==-1:
            return None
        g=G
        b=a
        a=p[a]
        g[a].remove(b)
        g[b].remove(a)

    return (a,b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )