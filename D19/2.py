class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

a=input().split()
n=int(a[0])
k=int(a[1])

if 1<=n<=100000 and 0<=k<=1000000000:
    b=input().split()
    head=None
    tail=None
    valid=True
    for i in b:
        e=int(i)
        if -1000000000<=e<=1000000000:
            new=Node(e)
            if head==None:
                head=new
                tail=new
            else:
                tail.next=new
                new.prev=tail
                tail=new
        else:
            valid=False
    if valid==True:
        k=k%n
        for i in range(k):
            newtail=tail.prev
            newtail.next=None
            tail.prev=None
            tail.next=head
            head.prev=tail
            head=tail
            tail=newtail
        temp=head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
    else:
        print("Invalid Input")
else:
    print("Invalid Input")