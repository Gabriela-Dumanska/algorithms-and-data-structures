from kol1btesty import runtests

def partition(A,p,k):
   pivot=A[k]
   counter=p-1
   for i in range(p,k):
       if A[i]>=pivot:
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



def f(T):
    for i in range(len(T)):
        T[i]=quick_sort(list(T[i]),0,len(T[i])-1)
    quick_sort(T,0,len(T)-1)
    T+=['a']
    Result=0
    counter=0
    i=0
    while i<len(T)-1:
        if T[i+1]==T[i]:
            counter+=1
        else:
            counter+=1
            Result=max(Result,counter)
            counter=0
        i+=1

    return Result

T =["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]

#f(T)
# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True )
