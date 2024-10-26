class Node():
   def __init__(self,val):
        self.val=val 
        self.next=None

first=None
p=Node(2)
p.next=first
first=p
p=Node(4)
p.next=first
first=p
p=Node(2)
p.next=first
first=p
p=Node(57)
p.next=first
first=p
p=Node(1)
p.next=first
first=p
p=Node(3)
p.next=first
first=p
p=Node(12)
p.next=first
first=p
p=Node(8)
p.next=first
first=p


def cut(P):
    if P==None:
        return None,None,None
    p=P
    k=P
    while k.next!=None and k.val<=k.next.val:
        #print(k.val)
        k=k.next
    P=k.next
    k.next=None
    return(p,k,P)

def merge(p1,p2):
    if p1==None:
        return p2
    if p2==None:
        return p1
    head=t=Node(None)

    while p1 and p2:
        if p1.val<=p2.val:
            t.next=p1
            p1=p1.next
        else:
            t.next=p2
            p2=p2.next
        t=t.next

    while p1:
        t.next=p1
        p1=p1.next
        t=t.next
    while p2:
        t.next=p2
        p2=p2.next
        t=t.next
    return head.next,t

def sort(P):
    t=P
    while t.next!=None:
        t=t.next

    while True:
        p1,k1,P=cut(P) 
        p2,k2,P=cut(P)
        
       
        if p2==None:
            return p1


        p,k=merge(p1,p2)


        if P==None:
            
            P=p
            t=k
        #print(p.val, k.val)
        else:
            t.next=p 
            t=k


p=sort(first)

while p is not None:
    print(p.val)
    p=p.next