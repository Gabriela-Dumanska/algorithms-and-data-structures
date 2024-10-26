'''
GABRIELA DUMAŃSKA
Algorytm oblicza opcje dojazdu n razy, a każda z nich to najtańsza opcja dojazdu, gdyby wykorzystać wyjątek
przy dojeździe na i-ty parking. Algorytm oblicza jak najtaniej dojechać do i-tego parkingu przez znalezienie minimum 
spośród T poprzednich kilometrów.

Złożoność ponad n^2.
'''
from zad9testy import runtests
from math import inf 

def min_cost( O, C, T, L ):
    O.append(0)
    C.append(0)
    O.append(L)
    C.append(0)
    O, C = zip(*sorted(zip(O, C)))
    n=len(O)
    B=[inf for _ in range (n)]
    B[0]=0
    for j in range(1,n):
            p=inf
            t=T
            x=j-1
            while x>=0 and O[j]-t<=O[x]:
                    p=min(p,B[x]+C[x])
                    x-=1
            B[j]=p
    mini=inf
    for i in range (1,n):
        R=B.copy()
        for j in range(i,n):
            p=inf
            t=T
            if i==j:
                t=2*T
            x=j-1
            while x>=0 and O[j]-t<=O[x]:
                    p=min(p,R[x]+C[x])
                    x-=1
            R[j]=p
        mini=min(mini,R[-1])
        
    return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )
