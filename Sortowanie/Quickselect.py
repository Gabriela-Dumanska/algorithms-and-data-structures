from statistics import median
def partition(A,p,k):
   pivot=median([A[p],A[(p+k)//2],A[k]])
   if pivot==A[p]: m=p
   if pivot==A[k]: m=k
   else: m=(p+k)//2
   A[m],A[k]=A[k],A[m]
   counter=p-1
   for i in range(p,k):
       if A[i]<=pivot:
           counter+=1
           A[counter],A[i]=A[i],A[counter]    
   counter+=1
   A[counter],A[k]=A[k],A[counter]
   return counter

def quickselect(A,p,k,x):
    if p==k:
        return A[p]
    q=partition(A,p,k)
    if q==x:
        return A[q]
    if q<x:
        return quickselect(A,q+1,k,x)
    else:
        return quickselect(A,p,q-1,x)
    
print(quickselect([7,4,2,9,0,17,74],0,6, 5))