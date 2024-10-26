from zad6testy import runtests

from queue import Queue

def binworker( M ):
    m=len(M)
    G=[[] for _ in range (2*m+5)]

    for i in range(m):
        for j in range(len(M[i])):
            G[i].append(M[i][j]+m)

    def colorize_vertices(G):
        n = len(G)
        
        # 0 means no color (we will use 2 colors as we want to divide vertices 
        # into two disjoint sets)
        colors = [0] * n  
        
        def dfs(u):
            for v in G[u]:
                if not colors[v]:
                    colors[v] = -1 * colors[u]
                    if not dfs(v): return False
                elif colors[v] == colors[u]:
                    return False
            return True

        for u in range(n):
            if not colors[u]:
                colors[u] = 1
                if not dfs(u): return []  # Return an empty list if a graph is not bipartite

        return colors


    def bfs(G, s, t, parents, visited, token):
        n = len(G)
        q = Queue()
        q.put(s)
        visited[s] = token
        
        while not q.empty():
            u = q.get()
            for v in range(n):
                if not G[u][v] or visited[v] == token: continue
                q.put(v)
                visited[v] = token
                parents[v] = u
        
        return visited[t] == token


    def get_bottleneck(G, s, t, parents):
        bottleneck = float('inf')
        u = t
        while u != s:
            bottleneck = min(bottleneck, G[parents[u]][u])
            u = parents[u]
        return bottleneck


    def update_flow(G, s, t, parents, bottleneck):
        v = t
        while v != s:
            u = parents[v]
            G[u][v] -= bottleneck
            G[v][u] += bottleneck
            v = parents[v]

            
    def create_residual_graph(G, colors):
        n = len(G)
        G2 = [[0] * (n + 2) for _ in range(n + 2)]
        
        # Add residual undirected edges
        for u in range(n):
            for v in G[u]:
                G2[u][v] = 1
        
        # Add directed edges from source to all vertices
        for u in range(n):
            if colors[u] == 1:
                G2[u][n + 1] = 1
            else:
                G2[n][u] = 1
        
        return G2, n, n + 1
        

    def edmonds_karp(RG, s, t):
        n = len(RG)
        max_flow = 0
        parents = [-1] * n
        visited = [0] * n
        token = 1
        
        while bfs(RG, s, t, parents, visited, token):
            # Find an augmenting path and its bottleneck value
            bottleneck = get_bottleneck(RG, s, t, parents)
            # Update flow on a path which was found
            update_flow(RG, s, t, parents, bottleneck)
            # Increase a value of the maximum flow
            max_flow += bottleneck
            token += 1
                
        return max_flow


    def maximum_association(G):
        colors = colorize_vertices(G)
        # If a graph is not bipartite, return -1
        if not colors: return -1
        RG, s, t = create_residual_graph(G, colors)
        print(RG,s,t)
        return edmonds_karp(RG, s, t)
    return maximum_association(G)
# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( binworker, all_tests = False )
print(binworker( [ [ 0, 1, 3], 
[ 2, 4], 
[ 0, 2], 
[ 3 ], 
[ 3, 2] ]))
