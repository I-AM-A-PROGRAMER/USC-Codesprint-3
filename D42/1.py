class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
n=int(input())
if 2<=n<=10000:
    a=input().split()
    nodes=[]
    valid=True
    for i in a:
        e=int(i)
        if e==-1:
            nodes.append(None)
        elif -1000000000<=e<=1000000000:
            nodes.append(Node(e))
        else:
            valid=False
    if valid==True:
        for i in range(n):
            if nodes[i]!=None:
                l=2*i+1
                r=2*i+2
                if l<n:
                    nodes[i].left=nodes[l]
                if r<n:
                    nodes[i].right=nodes[r]
        root=nodes[0]
        first=None
        second=None
        prev=None
        cur=root
        while cur!=None:
            if cur.left==None:
                if prev!=None and prev.data>cur.data:
                    if first==None:
                        first=prev
                    second=cur
                prev=cur
                cur=cur.right
            else:
                p=cur.left
                while p.right!=None and p.right!=cur:
                    p=p.right
                if p.right==None:
                    p.right=cur
                    cur=cur.left
                else:
                    p.right=None
                    if prev!=None and prev.data>cur.data:
                        if first==None:
                            first=prev
                        second=cur
                    prev=cur
                    cur=cur.right
        t=first.data
        first.data=second.data
        second.data=t
        for i in range(n):
            if nodes[i]==None:
                print(-1,end=" ")
            else:
                print(nodes[i].data,end=" ")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")