class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
n=int(input())
if 1<=n<=100000:
    a=input().split()
    root=None
    valid=True
    for i in a:
        x=int(i)
        if -1000000000<=x<=1000000000:
            node=Node(x)
            if root==None:
                root=node
            else:
                cur=root
                while True:
                    if x<cur.data:
                        if cur.left==None:
                            cur.left=node
                            break
                        cur=cur.left
                    else:
                        if cur.right==None:
                            cur.right=node
                            break
                        cur=cur.right
        else:
            valid=False
    k=int(input())
    if 1<=k<=n and valid==True:
        st=[]
        cur=root
        c=0
        while len(st)>0 or cur!=None:
            while cur!=None:
                st.append(cur)
                cur=cur.right
            cur=st.pop()
            c=c+1
            if c==k:
                print(cur.data)
                break
            cur=cur.left
    else:
        print("Invalid Input")
else:
    print("Invalid Input")