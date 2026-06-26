n=int(input())
if 1<=n<=200000:
    a=input().split()
    val=[0]
    valid=True
    for i in a:
        e=int(i)
        if 1<=e<=1000000000:
            val.append(e)
        else:
            valid=False
    g=[]
    for i in range(n+1):
        g.append([])
    for i in range(n-1):
        b=input().split()
        u=int(b[0])
        v=int(b[1])
        if 1<=u<=n and 1<=v<=n:
            g[u].append(v)
            g[v].append(u)
        else:
            valid=False
    if valid==True:
        vis=[0]*(n+1)
        level=[0]*(n+1)
        q=[1]
        vis[1]=1
        front=0
        ans=0
        while front<len(q):
            x=q[front]
            front=front+1
            if level[x]%2==0:
                ans=ans+val[x]
            for i in g[x]:
                if vis[i]==0:
                    vis[i]=1
                    level[i]=level[x]+1
                    q.append(i)
        print(ans)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")