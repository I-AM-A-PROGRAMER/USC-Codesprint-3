import heapq
a=input().split()
n=int(a[0])
m=int(a[1])
if 1<=n<=100000 and 1<=m<=200000:
    g=[]
    valid=True
    for i in range(n+1):
        g.append([])
    for i in range(m):
        b=input().split()
        u=int(b[0])
        v=int(b[1])
        t=int(b[2])
        e=int(b[3])
        if 1<=u<=n and 1<=v<=n and 1<=t<=1000000 and 1<=e<=1000000000:
            g[u].append([v,t,e])
        else:
            valid=False
    if valid==True:
        inf=10**18
        d=[inf]*(n+1)
        d[1]=0
        h=[]
        heapq.heappush(h,[0,1])
        while len(h)>0:
            x=heapq.heappop(h)
            dis=x[0]
            u=x[1]
            if dis!=d[u]:
                continue
            for i in g[u]:
                v=i[0]
                t=i[1]
                e=i[2]
                if dis<e and dis+t<d[v]:
                    d[v]=dis+t
                    heapq.heappush(h,[d[v],v])
        for i in range(1,n+1):
            if d[i]==inf:
                print(-1,end=" ")
            else:
                print(d[i],end=" ")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")