from zad1testy import runtests

'''
Gabriela Dumańska

Algorytm dla litery a słowa s szuka palindromu, który miałby środek w a. Zapisuje promień do tablicy P.
Gdy jest niezerowy, wykorzystuje symetrię w palindromach i wcześniej uzupełnioną tablicę P- 
przepisuje w odpowiedni sposób promienie na prawo od środka a i kontynuuje pracę za palindromem. 
Powtarza ten proces, aż uzupełni całą tablicę. Na bieżąco aktualizuje informację o maksymalnym palindromie.

Obstawiam złożoność rzędu O(n), gdzie n to długość słowa, ponieważ algorytm przechodzi po słowie tylko raz.
'''
def ceasar( s ):
    s="0"+s
    N=len(s)
    P=[0]*N
    i=2
    r=0
    maxi=0
    while i<N:
        while i-r-1>0 and i+r+1<N and s[i-r-1]==s[i+r+1]:
            r+=1 
        P[i]=r
        if 2*r+1>maxi:
            maxi=2*r+1
        q=1
        while q<r:
            if P[i-q]==r-q:
                break;
            P[i+q]=min(P[i-q],r-q)
            if 2*P[i+q]+1>maxi:
                maxi=2*P[i+q]+1
            q+=1
        r=max(0,r-q)
        i=i+q

    return maxi

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ceasar , all_tests = True )


