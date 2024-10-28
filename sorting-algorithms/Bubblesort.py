def bubblesort(a):
    n=len(a)
    change=True
    while change:
        change=False
        for i in range (n-1):
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                change=True
a=[9,8,7,6,5,4,3,2,1]
bubblesort(a)
print(a)