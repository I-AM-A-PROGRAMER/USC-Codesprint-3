def dfs(x,p):
    global t
    tin[x]=t
    arr[t]=val[x]
    t=t+1
    for i in g[x]:
        if i!=p:
            dfs(i,x)
    tout[x]=t-1
a=input().split()
n=int(a[0])
q=int(a[1])
if 1<=n<=200000 and 1<=q<=200000:
    b=input().split()
    val=[0]
    valid=True
    for i in b:
        e=int(i)
        if 1<=e<=1000000000:
            val.append(e)
        else:
            valid=False
    g=[]
    for i in range(n+1):
        g.append([])
    for i in range(n-1):
        c=input().split()
        u=int(c[0])
        v=int(c[1])
        if 1<=u<=n and 1<=v<=n:
            g[u].append(v)
            g[v].append(u)
        else:
            valid=False
    if valid==True:
        tin=[0]*(n+1)
        tout=[0]*(n+1)
        arr=[0]*n
        t=0
        dfs(1,0)
        bit=[0]*(n+1)
        for i in range(n):
            j=i+1
            while j<=n:
                bit[j]=bit[j]+arr[i]
                j=j+(j&-j)
        for i in range(q):
            c=input().split()
            if c[0]=="1":
                x=int(c[1])
                v=int(c[2])
                diff=v-val[x]
                val[x]=v
                j=tin[x]+1
                while j<=n:
                    bit[j]=bit[j]+diff
                    j=j+(j&-j)
            else:
                x=int(c[1])
                s1=0
                j=tout[x]+1
                while j>0:
                    s1=s1+bit[j]
                    j=j-(j&-j)
                s2=0
                j=tin[x]
                while j>0:
                    s2=s2+bit[j]
                    j=j-(j&-j)
                print(s1-s2)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")