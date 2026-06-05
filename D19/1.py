class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

n=int(input())
if 1<=n<=100000:
    a=input().split()
    k=int(input())
    if 1<=k<=100000:
        head=None
        tail=None
        for i in a:
            new=Node(int(i))
            if head==None:
                head=new
                tail=new
            else:
                tail.next=new
                tail=new
        tail.next=head

        curr=head
        prev=tail

        while curr.next!=curr:
            for i in range(k-1):
                prev=curr
                curr=curr.next

            prev.next=curr.next
            curr=curr.next

        print(curr.data)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")