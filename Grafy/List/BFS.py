from collections import deque
#przeszukiwanie grafu wszerz
#O(V+E)
def BFS(G,root):
    visited=[False]*len(G)
    Q=deque()
    visited[root]=True
    Q.append(root)
    while len(Q):
        u=Q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v]=True
                Q.append(v)
    return visited

G = [[1,2],[2,0,6],[0,1],[4,5],[3,5],[3,4],[7],[]]

Result= BFS(G,5)
print(Result)
