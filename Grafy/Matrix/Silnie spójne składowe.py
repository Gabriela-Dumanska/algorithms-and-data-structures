#jest maksymalnym podgrafem, w którym istnieją ścieżki pomiędzy każdymi dwoma wierzchołkami

def transpone_graph(G):
    Q=[[0 for _ in range(len(G))] for _ in range(len(G))]
    for u in range(len(G)):
        for v in range(len(G)):
            if G[u][v]==1:
                Q[v][u]=1
    return Q

def first_DFS(G):
    visited=[False  for _ in range(len(G))]
    stack=[]
    def dfs_visit(u):
        visited[u]=True
        for v in range (len(G)):
            if not visited[v] and G[u][v]!=0:
                dfs_visit(v)
        stack.append(u)
    for u in range(len(G)):
        if not visited[u]:
            dfs_visit(u)
    return stack

def second_DFS(G,stack):
    visited=[False for _ in range (len(G))]
    Result=[]
    def dfs_visit(u):
        visited[u]=True
        for v in range(len(G)):
            if not visited[v] and G[u][v]!=0:
                components.append(v)
                dfs_visit(v)
    while len(stack):
        u=stack.pop()
        if not visited[u]:
            components=[]
            components.append(u)
            dfs_visit(u)
            Result.append(components)
    return Result

def strongly_connected_compontents(G):
    stack=first_DFS(G)
    G=transpone_graph(G)
    result=second_DFS(G,stack)
    return result

G=[[0,1,0,0,0,0,0,0],
   [0,0,1,0,0,0,0,0],
   [1,0,0,1,0,0,0,0],
   [0,0,0,0,1,0,0,0],
   [0,0,0,0,0,1,0,1],
   [0,0,0,0,0,0,1,0],
   [0,0,0,0,1,0,0,1],
   [0,0,0,0,0,0,0,0]
   ]
print(strongly_connected_compontents(G))




