from zad2testy import runtests
'''
Gabriela Dumanska

Algorytm sortuje tablice sniegu. Dodaje do wyniku kolejne maksymalne wartosci i odejmuje od nich licznik dni. Jest to mozliwe, poniewaz
dodawanie jest przemienne- stopiony snieg do odjecia jest stala wartoscia i mozemy odejmowac go w dowolnym momencie. Mozemy rowniez
do wyniku dodawac same najwieksze wartosci (pomijajac ich miejsce w wawozie), poniewaz przeprowadzajac symulacje 
uwzgledniajaca miejsce w wawozie wystarczyloby zbierac kolejno od kierunkow wjazdu czynniki, ktore wczesniej byly potrzebne do sumy
Tym sposobem nie zniszczymy zadnego potrzebnego sniegu. Dodatkowym usprawnieniem jest przerwanie sortowania tablicy, gdy sortowane
wartosci sa juz stopione, czyli mniejsze od licznika dni.
'''
def parent(i): return (i-1)//2
def left(i): return 2*i+1
def right(i): return 2*i+2

def heapify(A,i,n):
    l=left(i)
    r=right(i)
    maxi=i

    if l<n and A[l]>A[maxi]: maxi=l
    if r<n and A[r]>A[maxi]: maxi=r

    if i!=maxi:
        A[i],A[maxi]=A[maxi],A[i]
        heapify(A,maxi,n)

def buildheap(A):
    n=len(A)
    for i in range(parent(n-1),-1,-1):
        heapify(A,i,n)

def heapsort(A):
    result=0
    days=0
    n=len(A)
    buildheap(A)
    for i in range (n-1,0,-1):
        A[0],A[i]=A[i],A[0]
        if A[i]-days>0:
            result+=A[i]-days
            days+=1
        else:
            return result
        heapify(A,0,i)

def snow( S ):
   return(heapsort(S))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
