def DFS_tree(G,root):
    visited=[False]*len(G)
    Result=[root]
    def dfs_visit(G,u):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                Result.append(v)
                dfs_visit(G,v)
    dfs_visit(G,root)
    return Result
G = [[1,4],[2,3],[0,7],[4],[5],[3,6],[3],[8],[9],[10],[6,7]]

Result= DFS_tree(G,0)
print(Result)