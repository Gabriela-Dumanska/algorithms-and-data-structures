#Graf skierowany
from collections import deque

def BFS(G,root,colours,colour):
    Q=deque()
    colours[root]=colour
    Q.append(root)
    while len(Q):
        u=Q.popleft()
        for v in G[u]:
            if colours[v]==None:
                colours[v]=colour
                Q.append(v)
    return

def connected_components(G):
    colours=[None]*len(G)
    colour=0
    for i in range (len(G)):
        if colours[i]==None:
            BFS(G,i,colours,colour)
            colour+=1
    if colour>1:
        return False, colours
    return True

print(connected_components([[1,2],[2,0],[1,0],[4,5],[3,5],[3,4],[]]))