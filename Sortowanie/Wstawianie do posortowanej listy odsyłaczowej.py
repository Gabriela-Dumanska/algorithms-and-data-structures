class Node():
   def __init__(self,val):
        self.val=val 
        self.next=None
first=None
for i in range (10,0,-2):
    p=Node(i)
    p.next=first
    first=p

def insert(first,a):
    if first==None:
        return Node(a)
    if a<first.val:
        A=Node(a)
        A.next=first
        return A
    prev=first
    cur=first.next
    while cur!=None and cur.val<a:
        prev=cur
        cur=cur.next
    prev.next=Node(a)
    prev.next.next=cur
    return first


p=insert(first,9)

while p is not None:
    print(p.val)
    p=p.next