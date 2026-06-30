a=input().split()
n=int(a[0])
m=int(a[1])
if 2<=n<=18 and 1<=m<=n*(n-1)//2:
    g=[]
    valid=True
    for i in range(n):
        g.append([])
    for i in range(m):
        b=input().split()
        u=int(b[0])-1
        v=int(b[1])-1
        if 0<=u<n and 0<=v<n:
            g[u].append(v)
            g[v].append(u)
        else:
            valid=False
    if valid==True:
        dp=[]
        for i in range(1<<n):
            dp.append([0]*n)
        for i in range(n):
            dp[1<<i][i]=1
        for mask in range(1<<n):
            for u in range(n):
                if dp[mask][u]==1:
                    for v in g[u]:
                        if (mask&(1<<v))==0:
                            dp[mask|(1<<v)][v]=1
        ok=False
        for i in range(n):
            if dp[(1<<n)-1][i]==1:
                ok=True
                break
        if ok==True:
            print("MISSION POSSIBLE")
        else:
            print("MISSION FAILED")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")