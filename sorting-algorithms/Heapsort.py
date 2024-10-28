def parent(i): return (i-1)//2
def left(i): return 2*i+1
def right(i): return 2*i+2
def heapify(A,i,n):
    l=left(i)
    r=right(i)
    maxi=i
    if l<n and A[l]>A[maxi]: maxi=l
    if r<n and A[r]>A[maxi]: maxi=r

    if maxi!=i:
        A[i],A[maxi]=A[maxi],A[i]
        heapify(A,maxi,n)
def buildheap(A):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,i,n)

def heapsort(A):
    n=len(A)
    buildheap(A)

    for i in range(n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        heapify(A,0,i)

A=[9,8,7,6,5,4,3,2,1]
heapsort(A)
print(A)

