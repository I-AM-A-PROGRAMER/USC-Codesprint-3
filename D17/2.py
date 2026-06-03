class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input())
if 1<=n<=100000:
    a=input().split()
    k=int(input())
    if 1<=k<=n:
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
            c=0
            temp=head
            while temp!=None:
                c=c+1
                temp=temp.next
            pos=c-k+1
            if pos==1:
                head=head.next
            else:
                temp=head
                for i in range(pos-2):
                    temp=temp.next
                temp.next=temp.next.next
            temp=head
            while temp!=None:
                print(temp.data,end=" ")
                temp=temp.next
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")