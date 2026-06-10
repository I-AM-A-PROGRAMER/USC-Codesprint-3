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
            node=Node(e)
            if head==None:
                head=node
                tail=node
            else:
                tail.next=node
                tail=node
        else:
            valid=False
    if valid==True:
        slow=head
        fast=head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")