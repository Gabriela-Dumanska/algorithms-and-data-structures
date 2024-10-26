def lis(T):
    n=len(T)
    Result=[1]*n
    for i in range (n):
        for j in range(i):
            if T[j]<T[i] :
                Result[i]=max(Result[i],Result[j]+1)
    return max(Result)

print(lis([13, 7, 21, 42, 8, 2, 44, 53]))

    