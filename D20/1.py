class Node:
    def __init__(self,k,v):
        self.key=k
        self.val=v
        self.prev=None
        self.next=None
c=int(input())
q=int(input())
head=Node(0,0)
tail=Node(0,0)
head.next=tail
tail.prev=head
d={}
for i in range(q):
    a=input().split()
    if a[0]=="PUT":
        key=int(a[1])
        val=int(a[2])
        if key in d:
            node=d[key]
            node.prev.next=node.next
            node.next.prev=node.prev
            node.val=val
            node.next=head.next
            node.prev=head
            head.next.prev=node
            head.next=node
        else:
            if len(d)==c:
                node=tail.prev
                del d[node.key]
                node.prev.next=tail
                tail.prev=node.prev
            node=Node(key,val)
            d[key]=node
            node.next=head.next
            node.prev=head
            head.next.prev=node
            head.next=node
    else:
        key=int(a[1])
        if key not in d:
            print(-1)
        else:
            node=d[key]
            node.prev.next=node.next
            node.next.prev=node.prev
            node.next=head.next
            node.prev=head
            head.next.prev=node
            head.next=node
            print(node.val)