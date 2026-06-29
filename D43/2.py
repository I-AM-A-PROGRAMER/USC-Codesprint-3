a=input().split()
n=int(a[0])
m=int(a[1])
if 2<=n<=2500 and 1<=m<=5000:
    edges=[]
    g=[]
    rg=[]
    valid=True
    for i in range(n+1):
        g.append([])
        rg.append([])
    for i in range(m):
        b=input().split()
        u=int(b[0])
        v=int(b[1])
        w=int(b[2])
        if 1<=u<=n and 1<=v<=n and -1000000000<=w<=1000000000:
            edges.append([u,v,w])
            g[u].append(v)
            rg[v].append(u)
        else:
            valid=False
    if valid==True:
        vis1=[0]*(n+1)
        q=[1]
        vis1[1]=1
        front=0
        while front<len(q):
            x=q[front]
            front=front+1
            for i in g[x]:
                if vis1[i]==0:
                    vis1[i]=1
                    q.append(i)
        vis2=[0]*(n+1)
        q=[n]
        vis2[n]=1
        front=0
        while front<len(q):
            x=q[front]
            front=front+1
            for i in rg[x]:
                if vis2[i]==0:
                    vis2[i]=1
                    q.append(i)
        neg=-10**18
        d=[neg]*(n+1)
        d[1]=0
        for i in range(n-1):
            for e in edges:
                u=e[0]
                v=e[1]
                w=e[2]
                if d[u]!=neg and d[u]+w>d[v]:
                    d[v]=d[u]+w
        ok=False
        for e in edges:
            u=e[0]
            v=e[1]
            w=e[2]
            if d[u]!=neg and d[u]+w>d[v] and vis1[u]==1 and vis2[v]==1:
                ok=True
                break
        if ok==True:
            print("INFINITE PROFIT")
        elif d[n]==neg:
            print("UNREACHABLE")
        else:
            print(d[n])
    else:
        print("Invalid Input")
else:
    print("Invalid Input")