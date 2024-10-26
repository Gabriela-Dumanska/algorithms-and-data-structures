def longest(T):
    palindrom=(0,0)
    maxi=0
    Result=[[0 for _ in range (len(T))] for _ in range(len(T)) ]
    for i in range(0,len(T)):
        for j in range(i, -1,-1):
            if i==j:
                Result[j][i]=1
            elif i-1==j:
                if T[i]==T[j]:
                    Result[j][i]=2
                else:
                    Result[j][i]=0
            else:
                if T[i]!=T[j]:
                    Result[j][i]=0
                else:
                    if j+1<len(T) and Result[j+1][i-1]:
                        Result[j][i]=Result[j+1][i-1]+2
                    else:
                        Result[j][i]=0
            if Result[j][i]>maxi:
                maxi=Result[j][i]
                palindrom=(j,i)
    print(maxi)
    print(T[palindrom[0]:palindrom[1]+1])
longest("abcccbcccbdabaabbbcbaaccb")
