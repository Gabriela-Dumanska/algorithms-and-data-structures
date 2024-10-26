from zad3testy import runtests
from statistics import median
def partition(A,p,k):
   pivot=median([A[p][1],A[(p+k)//2][1],A[k][1]])
   if pivot==A[p][1]: m=p
   if pivot==A[k][1]: m=k
   else: m=(p+k)//2
   A[m],A[k]=A[k],A[m]
   counter=p-1
   for i in range(p,k):
       if A[i][1]>pivot:
           counter+=1
           A[counter],A[i]=A[i],A[counter]    
   counter+=1
   A[counter],A[k]=A[k],A[counter]
   return counter
   
def quick_sort(A,p,k):
    while p<k:
        q=partition(A,p,k)
        if q-p<k-q:
            quick_sort(A,p,q-1)
            p=q+1
        else:
            quick_sort(A,q+1,k)
            k=q-1
    return A

def tasks(T):
    Order=[]
    for a in range(len(T)):
        pom=0
        for b in range(len(T)):
            if T[a][b]==1: pom+=1
            if T[a][b]==2: pom-=1
        Order.append((a,pom))
    Order=quick_sort(Order,0,len(Order)-1)
    Result=[]
    for i in range(len(Order)):
        Result.append(Order[i][0])
    return Result

    

T = [ [0,2,1,1], [1,0,1,1], [2,2,0,1], [2,2,2,0] ]
#print(tasks(T))
runtests(tasks)
