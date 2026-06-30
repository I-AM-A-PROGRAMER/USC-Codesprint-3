p=int(input())
if 1<=p<=200000:
    ind={}
    out={}
    g={}
    nodes=set()
    valid=True
    for i in range(p):
        a=input().split()
        if len(a)!=2:
            valid=False
        else:
            u=a[0]
            v=a[1]
            nodes.add(u)
            nodes.add(v)
            if u not in out:
                out[u]=0
            out[u]=out[u]+1
            if v not in ind:
                ind[v]=0
            ind[v]=ind[v]+1
            if u not in g:
                g[u]=[]
            g[u].append(v)
            if v not in g:
                g[v]=[]
    if valid==True:
        s=0
        e=0
        for i in nodes:
            x=0
            y=0
            if i in out:
                x=out[i]
            if i in ind:
                y=ind[i]
            if x-y==1:
                s=s+1
            elif y-x==1:
                e=e+1
            elif x!=y:
                valid=False
                break
        if valid==True and ((s==1 and e==1) or (s==0 and e==0)):
            print("ASSEMBLY POSSIBLE")
        else:
            print("ASSEMBLY IMPOSSIBLE")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")