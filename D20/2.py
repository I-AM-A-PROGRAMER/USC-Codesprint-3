class Node:
    def __init__(self,data):
        self.data=data
        self.npx=0

n=int(input())
if 1<=n<=100000:
    a=input().split()
    nodes=[]
    d={}
    valid=True
    for i in a:
        e=int(i)
        if 1<=e<=1000000000:
            node=Node(e)
            nodes.append(node)
            d[id(node)]=node
        else:
            valid=False
    if valid==True:
        for i in range(n):
            prev=0
            nxt=0
            if i>0:
                prev=id(nodes[i-1])
            if i<n-1:
                nxt=id(nodes[i+1])
            nodes[i].npx=prev^nxt
        prev=0
        curr=id(nodes[0])
        while curr:
            node=d[curr]
            print(node.data,end=" ")
            nxt=prev^node.npx
            prev=curr
            curr=nxt
    else:
        print("Invalid Input")
else:
    print("Invalid Input")