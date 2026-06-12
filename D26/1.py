class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.random=None
n=int(input())
if 1<=n<=100000:
    a=input().split()
    r=input().split()
    nodes=[]
    valid=True
    for i in a:
        e=int(i)
        if 1<=e<=1000000000:
            nodes.append(Node(e))
        else:
            valid=False
    if valid==True:
        for i in range(n-1):
            nodes[i].next=nodes[i+1]
        for i in range(n):
            x=int(r[i])
            if x!=-1:
                nodes[i].random=nodes[x]
        d={}
        for i in range(n):
            d[nodes[i]]=Node(nodes[i].data)
        for i in range(n):
            if nodes[i].next!=None:
                d[nodes[i]].next=d[nodes[i].next]
            if nodes[i].random!=None:
                d[nodes[i]].random=d[nodes[i].random]
        clone=[]
        temp=d[nodes[0]]
        while temp!=None:
            clone.append(temp)
            temp=temp.next
        for i in range(n):
            idx=-1
            if clone[i].random!=None:
                for j in range(n):
                    if clone[j]==clone[i].random:
                        idx=j
                        break
            print(clone[i].data,idx)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")