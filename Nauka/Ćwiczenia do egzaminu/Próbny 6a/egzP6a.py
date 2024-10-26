from egzP6atesty import runtests 

def partition(A,p,k):
   
   pivot=len(A[k])
   counter=p-1
   for i in range(p,k):
       if len(A[i])>pivot:
           counter+=1
           A[counter],A[i]=A[i],A[counter]    

       if len(A[i])==pivot:
           la=0
           lp=0
           for j in range (pivot):
               if ord(A[i][j])>96 and ord(A[i][j])<123:
                   la+=1
               if ord(A[k][j])>96 and ord(A[k][j])<123:
                   lp+=1
           if la>lp:
               counter+=1
               A[counter],A[i]=A[i],A[counter]  
                     
   counter+=1
   A[counter],A[k]=A[k],A[counter]
   return counter
   
def quick_sort(A,p,k,s):
    while p<k:
        q=partition(A,p,k)
        if q-p<k-q:
            quick_sort(A,p,q-1,s)
            p=q+1
        else:
            quick_sort(A,q+1,k,s)
            k=q-1
        if(p>s):
            return A
    return A

def google ( H, s ):
    quick_sort(H,0,len(H)-1,s)
    return H[s-1]

print(quick_sort( ['ab1','aba', 'abc', 'abab', 'a1a1', 'aa12a'],0,5,3))
#runtests ( google, all_tests=False )