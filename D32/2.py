a=input().split()
k=int(a[0])
q=int(a[1])
if 1<=k<=100000 and 1<=q<=100000:
    l=[0]*k
    front=0
    rear=0
    size=0
    for i in range(q):
        a=input().split()
        if a[0]=="ENQUEUE":
            x=int(a[1])
            if size==k:
                print("FULL")
            else:
                l[rear]=x
                rear=(rear+1)%k
                size=size+1
        elif a[0]=="DEQUEUE":
            if size==0:
                print("EMPTY")
            else:
                front=(front+1)%k
                size=size-1
        else:
            if size==0:
                print(-1)
            else:
                print(l[front])
else:
    print("Invalid Input")