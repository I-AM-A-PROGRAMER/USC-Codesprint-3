a=input().split()
n=int(a[0])
m=int(a[1])
if 1<=n<=100000 and 0<=m<=200000:
    g=[]
    for i in range(n+1):
        g.append([])
    valid=True
    for i in range(m):
        b=input().split()
        u=int(b[0])
        v=int(b[1])
        if 1<=u<=n and 1<=v<=n:
            g[u].append(v)
            g[v].append(u)
        else:
            valid=False
    if valid==True:
        color=[0]*(n+1)
        ok=True
        for i in range(1,n+1):
            if color[i]==0:
                q=[i]
                front=0
                color[i]=1
                while front<len(q):
                    x=q[front]
                    front=front+1
                    for j in g[x]:
                        if color[j]==0:
                            color[j]=3-color[x]
                            q.append(j)
                        elif color[j]==color[x]:
                            ok=False
                            break
                    if ok==False:
                        break
            if ok==False:
                break
        if ok==True:
            print("YES")
            for i in range(1,n+1):
                print(color[i],end=" ")
        else:
            print("NO")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")