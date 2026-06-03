class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input())
if 1<=n<=100000:
    a=input().split()
    head=None
    tail=None
    valid=True
    for i in a:
        e=int(i)
        if -1000000000<=e<=1000000000:
            new=Node(e)
            if head==None:
                head=new
                tail=new
            else:
                tail.next=new
                tail=new
        else:
            valid=False
    if valid==True:
        prev=None
        curr=head
        while curr!=None:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        head=prev
        temp=head
        while temp!=None:
            print(temp.data,end=" ")
            temp=temp.next
    else:
        print("Invalid Input")
else:
    print("Invalid Input")