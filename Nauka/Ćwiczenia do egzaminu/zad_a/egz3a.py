from egz3atesty import runtests
from statistics import median

def partition(A,p,k):
   pivot=median([A[p][0],A[(p+k)//2][0],A[k][0]])
   if pivot==A[p][0]: m=p
   if pivot==A[k][0]: m=k
   else: m=(p+k)//2
   pivot=A[m]
   A[m],A[k]=A[k],A[m]
   counter=p-1
   for i in range(p,k):
       if A[i][1]-A[i][0]<pivot[1]-pivot[0]:
           counter+=1
           A[counter],A[i]=A[i],A[counter]    
       elif A[i][1]-A[i][0]==pivot[1]-pivot[0]:
           if A[i][0]<pivot[0]:
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

def snow( T, I ):
    I=quick_sort(I,0,len(I)-1)
    print(I)


# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( snow, all_tests = True )
I = [(3, 10), (0, 5), (3,4),(20, 30), (25, 35), (26, 26), (25,36)]
print(snow(100,I))
