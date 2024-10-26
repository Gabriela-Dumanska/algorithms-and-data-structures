def Knapsack(P,W,w):
    n=len(W)
    Result=[[0 for _ in range (w+1)] for _ in range (n)]
    for i in range (W[0], w+1):
        Result[0][i]=P[0]
    
    for i in range(w+1):
        for j in range(1,n):
            Result[j][i]=Result[j-1][i]
            if i-W[j]>=0:
                Result[j][i]=max(Result[j][i], Result[j-1][i-W[j]]+P[j])
    return Result[n-1][w]
P = [10, 8, 4, 5, 3, 7]
W = [4, 5, 12, 9, 1, 13]
w = 24
print(Knapsack(P,W,w))
