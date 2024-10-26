#GABRIELA DUMAŃSKA
#Algorytm najpierw uzupełnia i-te pole zerowego wiersza ilością paliwa z całej plamy rozpoczynającej się w i. Następnie algorytm przesuwa się po zerowym wierszu tablicy.
#Jeśli na danym polu występuje plama, wstawiamy ją do kolejki priorytetowej. 
#Przesuwamy się jak najdalej, a gdy braknie paliwa, tankujemy pierwszą plamą z kolejki. Kolejka przechowuje wszystkie minione plamy- tą największą na czele.
#Tankowanie plamą, którą już minęliśmy oznacza tyle co: tam powinniśmy byli się zatrzymać i zatankować. 
#Zawsze opłaca nam się zatrzymać raz po największą plamę, niż kilka razy po mniejsze.
#Złożoność: O(m+p+plog p) p-liczba odrębnych plam ropy
from zad8testy import runtests
from queue import PriorityQueue

def splashes(T,i):
    n=0
    def fuel(i,j):
        nonlocal n
        n+=T[i][j]
        T[i][j]=0
        if i>0 and T[i-1][j]:
            fuel(i-1,j)
        if j>0 and T[i][j-1]:
            fuel(i,j-1)
        if i<len(T)-1 and T[i+1][j]:
            fuel(i+1,j)
        if j<len(T[0])-1 and T[i][j+1]:
            fuel(i,j+1)
    fuel(0,i)     
    return n

def collect(T):
    i=0
    while i<len(T[0]):
        if T[0][i]:
            T[0][i]=splashes(T,i)
        i+=1

def plan(T):
    B=len(T[0])
    Q=PriorityQueue()
    fuel=0
    stops=0
    collect(T)


    for i in range (B-1):
        if T[0][i]:
            Q.put((-T[0][i],i))
        if fuel==0:
            f,p=Q.get()
            fuel-=f
            stops+=1
        fuel-=1
    
    return stops


runtests(plan, all_tests=True)