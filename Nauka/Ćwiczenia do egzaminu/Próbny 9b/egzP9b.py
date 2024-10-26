from egzP9btesty import runtests

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
    return Result

def dyrektor( G, R ):
    for i in range(len(R)):
        for u in R[i]:
            G[i].remove(u)
    return Euler_cycle(G)

G = [
[1, 0, 2],
[2, 0],
[1, 0]
]
R = [
[0],
[],
[]
]



#print(dyrektor(G,R))
runtests(dyrektor, all_tests=True)