#Euler cycle is a path that visits every edge one time and starts and ends on the same vertex

def Euler_cycle(G):
    Result = []
    Stack=[0]
    current=0
    while Stack:
        if G[current]:
            Stack.append(current)
            u=G[current][0]
            G[current].remove(u)
            #G[u].remove(current) directed graph
            current=u
        else:
            Result.append(current)
            current=Stack.pop()
            
    Result.reverse()
    print(G)
    return Result


G = [[1,2],[0,6,3,4],[0,6,3,4],[1,2,4,5],
     [1,3,5,2],[4,3],[1,2]]

Result= Euler_cycle(G)
print(Result)