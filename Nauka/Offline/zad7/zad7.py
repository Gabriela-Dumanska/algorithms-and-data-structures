from zad7testy import runtests
from math import inf
def maze( L ):
    N=len(L)
    DP=[[-inf for _ in range(N)] for _ in range(N)]
    for i in range(N):
        if L[i][0]=='.':
            DP[i][0]=i+1
        else:
            break
    for j in range(1,N):
        for i in range(N-1,-1,-1):
            if L[i][j]=='.':
                if i+1<N and L[i+1][j]=='.' and L[i][j-1]=='.':
                    DP[i][j]=max(DP[i+1][j]+1, DP[i][j-1]+1)
                elif i+1<N and L[i+1][j]=='.':
                    DP[i][j]=DP[i+1][j]+1
                elif L[i][j-1]=='.':
                    DP[i][j]=DP[i][j-1]+1
        P=[-inf for _ in range(N)]
        for i in range(N):
            if L[i][j]=='.':
                if i-1>=0 and L[i-1][j]=='.' and L[i][j-1]=='.':
                    P[i]=max(P[i-1]+1, DP[i][j-1]+1)
                elif i-1>=0 and L[i-1][j]=='.':
                    P[i]=P[i-1]+1
                elif L[i][j-1]=='.':
                    P[i]=DP[i][j-1]+1
                DP[i][j]=max(DP[i][j],P[i])
    if DP[N-1][N-1]==-inf:
        return -1
    return DP[N-1][N-1]-1
L = [ "....",
"..#.",
"..#.",
"...." ]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
#print(maze(L))