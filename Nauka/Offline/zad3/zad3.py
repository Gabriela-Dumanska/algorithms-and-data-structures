from zad3testy import runtests

def change(T):
    for i in range (len(T)):
        p=0
        while p<len(T[i])-1 and T[i][p]==T[i][len(T[i])-1-p]:
            p+=1
        if T[i][p]<T[i][len(T[i])-1-p]:
            T[i]=T[i][::-1]

def partition(A,p,k):
   pivot=A[k]
   counter=p-1
   for i in range(p,k):
       if A[i]<=pivot:
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

def strong_string(T):
    change(T)
    maxi=0
    quick_sort(T,0,len(T)-1)
    
    for i in range (len(T)-1):
        counter=0
        while i<len(T)-1 and T[i]==T[i+1]:
            counter+=1
            i+=1
        if counter>maxi: maxi=counter
    
    return maxi+1


#print(strong_string(  ["pies", "mysz", "kot", "kogut", "tok", "seip", "kot"]))
# # zmien all_tests na True zeby uruchomic wszystkie testy
runtests( strong_string, all_tests=True)