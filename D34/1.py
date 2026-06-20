a=input().split()
n=int(a[0])
m=int(a[1])
if 1<=n<=100 and 1<=m<=100:
    l=[]
    q=[]
    fresh=0
    valid=True
    for i in range(n):
        b=input().split()
        row=[]
        for j in range(m):
            e=int(b[j])
            if e==0 or e==1 or e==2:
                row.append(e)
                if e==2:
                    q.append([i,j,0])
                elif e==1:
                    fresh=fresh+1
            else:
                valid=False
        l.append(row)
    if valid==True:
        front=0
        ans=0
        while front<len(q):
            x=q[front][0]
            y=q[front][1]
            t=q[front][2]
            front=front+1
            if t>ans:
                ans=t
            if x+1<n and l[x+1][y]==1:
                l[x+1][y]=2
                fresh=fresh-1
                q.append([x+1,y,t+1])
            if x-1>=0 and l[x-1][y]==1:
                l[x-1][y]=2
                fresh=fresh-1
                q.append([x-1,y,t+1])
            if y+1<m and l[x][y+1]==1:
                l[x][y+1]=2
                fresh=fresh-1
                q.append([x,y+1,t+1])
            if y-1>=0 and l[x][y-1]==1:
                l[x][y-1]=2
                fresh=fresh-1
                q.append([x,y-1,t+1])
        if fresh==0:
            print(ans)
        else:
            print(-1)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")