def solve(i,j,path):
    if i==n-1 and j==n-1:
        print(path)
        global found
        found=True
        return
    vis[i][j]=1
    if i+1<n and l[i+1][j]==1 and vis[i+1][j]==0:
        solve(i+1,j,path+"D")
    if j-1>=0 and l[i][j-1]==1 and vis[i][j-1]==0:
        solve(i,j-1,path+"L")
    if j+1<n and l[i][j+1]==1 and vis[i][j+1]==0:
        solve(i,j+1,path+"R")
    if i-1>=0 and l[i-1][j]==1 and vis[i-1][j]==0:
        solve(i-1,j,path+"U")
    vis[i][j]=0
n=int(input())
if 1<=n<=8:
    l=[]
    for i in range(n):
        a=input().split()
        row=[]
        for j in a:
            row.append(int(j))
        l.append(row)
    vis=[]
    for i in range(n):
        vis.append([0]*n)
    found=False
    if l[0][0]==1:
        solve(0,0,"")
    if found==False:
        print(-1)
else:
    print("Invalid Input")