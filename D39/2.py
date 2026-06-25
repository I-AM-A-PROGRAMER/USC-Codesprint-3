def solve(i,j,k):
    global found
    if k==len(w):
        found=True
        return
    if i<0 or i>=n or j<0 or j>=m:
        return
    if vis[i][j]==1 or l[i][j]!=w[k]:
        return
    vis[i][j]=1
    solve(i+1,j,k+1)
    solve(i-1,j,k+1)
    solve(i,j+1,k+1)
    solve(i,j-1,k+1)
    vis[i][j]=0
a=input().split()
n=int(a[0])
m=int(a[1])
if 1<=n<=6 and 1<=m<=6:
    l=[]
    valid=True
    for i in range(n):
        b=input().split()
        row=[]
        for j in b:
            if len(j)==1 and 'A'<=j<='Z':
                row.append(j)
            else:
                valid=False
        l.append(row)
    w=input()
    if 1<=len(w)<=15:
        for i in w:
            if i<'A' or i>'Z':
                valid=False
        if valid==True:
            vis=[]
            for i in range(n):
                vis.append([0]*m)
            found=False
            for i in range(n):
                for j in range(m):
                    if l[i][j]==w[0]:
                        solve(i,j,0)
            if found==True:
                print("YES")
            else:
                print("NO")
        else:
            print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")