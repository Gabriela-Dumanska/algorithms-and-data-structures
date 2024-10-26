from zad2testy import runtests
from math import inf, sqrt, ceil

def Kruskal_MST(E,lng):
    Unions=[i for i in range (lng)]
    def Find(u):
        if u!=Unions[u]:
            Unions[u]=Find(Unions[u])
        return Unions[u]
    
    def Union(u,v):
        u=Find(u)
        v=Find(v)
        if u==v:
            return False
        Unions[u]=v
        return True
    
    MST=[]
    for i in range(len(E)-1,-1,-1):
        u=E[i][0]
        v=E[i][1]
        if Union(u,v):
            MST.append(E[i])
    if len(MST)==lng-1:
        return MST[-1][2]
    return None
    

def highway(A):
    G=[[0 for _ in range (len(A))] for _ in range(len(A))]
    for u in range(len(A)):
        for v in range(u+1,len(A)):
                leng=ceil(sqrt((A[u][0]-A[v][0])**2+(A[u][1]-A[v][1])**2))
                G[u][v]=leng
                G[v][u]=leng
    E=[]
    for u in range(len (G)):
        for v in range (len(G)):
            if G[u][v]!=0:
                E.append((u,v,G[u][v]))
    E.sort(key=lambda x: x[2], reverse=True)
    Result=inf
    while True:
        maxi=Kruskal_MST(E,len(G))
        if maxi==None: break
        mini=E.pop()[2]
        E.pop()
        Result=min(maxi-mini,Result)
    return Result





A =[(10,10),(15,25),(20,20),(30,40)]
runtests(highway)
#highway(A)