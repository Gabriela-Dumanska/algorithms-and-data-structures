from collections import deque
#O(V^2)
def BFS(G,root):
    visited=[False for _ in range(len(G))]
    parent=[None for _ in range (len(G))]
    Q=deque()
    Result=[]
    visited[root]=True
    Q.append(root)
    while len(Q):
        u=Q.popleft()
        Result.append(u)
        for v in range (len(G)):
            if visited[v] is False and G[u][v]==1:
                Q.append(v)
                visited[v]=True
                parent[v]=u
    return Result

G =      [[0, 1, 0, 1, 1],
         [1, 0, 0, 1, 0],
         [0, 0, 0, 0, 1],
         [1, 1, 0, 0, 1],
         [1, 0, 1, 1, 0]]

print(BFS(G,0))

