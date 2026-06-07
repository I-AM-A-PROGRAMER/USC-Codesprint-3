class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
n=int(input())
if 1<=n<=100000:
    lists=[]
    for i in range(n):
        a=input().split()
        head=None
        tail=None
        for j in a:
            node=Node(int(j))
            if head==None:
                head=node
                tail=node
            else:
                tail.next=node
                tail=node
        lists.append(head)
    head=lists[0]
    for i in range(1,n):
        a=head
        b=lists[i]
        bot=Node(0)
        tail=bot
        while a!=None and b!=None:
            if a.data<=b.data:
                tail.next=a
                a=a.next
            else:
                tail.next=b
                b=b.next
            tail=tail.next
        if a!=None:
            tail.next=a
        else:
            tail.next=b
        head=bot.next
    temp=head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
else:
    print("Invalid Input")