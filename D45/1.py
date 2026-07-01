a=input().split()
n=int(a[0])
m=int(a[1])
if 1<=n<=200 and 0<=m<=n*n:
    inf=10**18
    d=[]
    for i in range(n):
        row=[]
        for j in range(n):
            if i==j:
                row.append(0)
            else:
                row.append(inf)
        d.append(row)
    valid=True
    for i in range(m):
        b=input().split()
        u=int(b[0])-1
        v=int(b[1])-1
        w=int(b[2])
        if 0<=u<n and 0<=v<n and 1<=w<=1000000:
            if w<d[u][v]:
                d[u][v]=w
        else:
            valid=False
    if valid==True:
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if d[i][k]+d[k][j]<d[i][j]:
                        d[i][j]=d[i][k]+d[k][j]
        q=int(input())
        if 1<=q<=100000:
            for i in range(q):
                b=input().split()
                u=int(b[0])-1
                v=int(b[1])-1
                if d[u][v]==inf:
                    print(-1)
                else:
                    print(d[u][v])
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")