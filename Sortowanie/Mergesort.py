from math import inf
def merge(T,p,m,k):
    L=[]
    R=[]
    
    for i in range(m-p+1):
        L.append(T[p+i])
    for i in range(k-m):
        R.append(T[m+i+1])
    L.append(inf)
    R.append(inf)
    i=j=0

    for q in range(p,k+1):
        if L[i]<=R[j]:
            T[q]=L[i]
            i+=1
        else:
            T[q]=R[j]
            j+=1

def mergesort(T,p,k):
    if p<k:
        m=(p+k)//2
        mergesort(T,p,m)
        mergesort(T,m+1,k)
        merge(T,p,m,k)

T=[9,8,7,6,5,4,3,2,1]
mergesort(T, 0 , len(T)-1)
print(T)
