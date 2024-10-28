#jest maksymalnym podgrafem, w którym istnieją ścieżki pomiędzy każdymi dwoma wierzchołkami
def first_DFS(G):
    stack=[]
    visited=[False]*len(G)
    def dfs_visit(G,u):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                dfs_visit(G,v)
        stack.append(u)
    for u in range(len(G)):
        if not visited[u]:
            dfs_visit(G,u)
    return stack

def transpose_graph(G):
    Q=[[] for _ in range (len(G))] 
    for i in range(len(G)):
        for j in G[i]:
            Q[j].append(i)
    return Q

def second_DFS(G,stack):
    visited=[False]*len(G)
    result=[]
    def dfs_visit(G,u):
        visited[u]=True
        for v in G[u]:
            if not visited[v]:
                components.append(v)
                dfs_visit(G,v)
    while len(stack):
        u=stack.pop()
        if not visited[u]:
            components=[]
            components.append(u)
            dfs_visit(G,u)
            result.append(components)
    return result

def strongly_connected_components(G):
    stack=first_DFS(G)
    G=transpose_graph(G)
    result=second_DFS(G,stack)
    return result

#print(strongly_connected_components([[1, 4], [2, 3], [0, 7], [4], [5], [3, 6], [3], [8], [9], [10], [6, 7]]))
print(strongly_connected_components([[1],[2],[0,2,8],[4,6],[5],[3],[5],[8],[9],[5,10],[7]]))