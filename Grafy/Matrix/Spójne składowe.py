from collections import deque

def BFS(G,root, colours, colour):
    Q=deque()
    colours[root]=colour
    Q.append(root)
    while len(Q):
        u=Q.popleft()
        for v in range (len(G)):
            if colours[v] is None and G[u][v]==1:
                colours[v]=colour
                Q.append(v)
    return

def connected_components(G):
    colours=[None]*len(G)
    colour=0
    for i in range (len(G)):
        if colours[i] is None:
            BFS(G,i,colours,colour)
            colour+=1
    if colour>1:
        return False, colours
    return True

G =      [[0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 0],
         [1, 1, 0, 0, 1],
         [1, 0, 0, 1, 0]]

print(connected_components(G))