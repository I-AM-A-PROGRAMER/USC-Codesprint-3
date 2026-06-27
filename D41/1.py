a=input().split()
m=int(a[0])
n=int(a[1])
if 1<=m<=1000 and 1<=n<=1000 and m*n<=1000000:
    l=[]
    valid=True
    for i in range(m):
        b=input().split()
        row=[]
        for j in b:
            e=int(j)
            if 1<=e<=100000:
                row.append(e)
            else:
                valid=False
        l.append(row)
    if valid==True:
        for d in range(m+n-1):
            t=[]
            r=0
            if d>=n:
                r=d-n+1
            c=d-r
            while r<m and c>=0:
                t.append(l[r][c])
                r=r+1
                c=c-1
            if d%2==0:
                t.reverse()
            for i in t:
                print(i,end=" ")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")