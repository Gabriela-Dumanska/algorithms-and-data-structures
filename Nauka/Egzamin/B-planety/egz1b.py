'''
GABRIELA DUMANSKA

    Z planety i patrz E lat świetlnych w tył. Dla wszystkich planet j w zasięgu E koszt polecenia z j na i to będzie minimum z:
    [(ile kosztowało mnie dolecenieć na j mając w baku q paliwa + (odległość z j do i - naddatek paliwa)* zatankowanie w j), gdzie q (1,10)
    oraz (jeśli jest z j do i teleport to: ile mnie kosztowało dolecieć do i bez naddatku paliwa + cena teleportu)]
    Rozwiązaniem będzie minimum z kolumny n-1.

    Złożoność: n*E^3

'''
from egz1btesty import runtests
from math import inf 
def planets( D, C, T, E ):
    Dp=[[inf for _ in range(len(D))] for _ in range(E)]
    
    for i in range(len(D)):
        for j in range(1,i):
            for q in range(1,E):
                for x in range (1,E):
                    Dp[q][i]=min(Dp[q][i], Dp[x][j]+abs(D[i]-D[j])) #niedokończone :(
    return 17

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = False )
