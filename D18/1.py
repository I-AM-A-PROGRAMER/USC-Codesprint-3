class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input())
if 1<=n<=100000:
    a=input().split()
    pos=int(input())
    if -1<=pos<n:
        l=[]
        head=None
        tail=None
        valid=True
        for i in a:
            e=int(i)
            if -1000000000<=e<=1000000000:
                new=Node(e)
                l.append(new)
                if head==None:
                    head=new
                    tail=new
                else:
                    tail.next=new
                    tail=new
            else:
                valid=False
        if valid==True:
            if pos!=-1:
                tail.next=l[pos]
            slow=head
            fast=head
            cycle=False
            while fast!=None and fast.next!=None:
                slow=slow.next
                fast=fast.next.next
                if slow==fast:
                    cycle=True
                    break
            if cycle==True:
                print("YES")
            else:
                print("NO")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")