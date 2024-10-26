def cycle(G):
    visited=[False]*len(G)
    parent=[None]*len(G)
    def dfs_visit(G,u):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                parent[v]=u
                dfs_visit(G,v)
            elif parent[u]!=v:
                return True
    for u in range(len(G)):
        if not visited[u]:
            if dfs_visit(G,u):
                return True
    return False

print(cycle( [[1, 2, 5], [0, 3], [0, 4, 7, 8], [1], [2, 6], [0], [4], [2], [2]]))
   