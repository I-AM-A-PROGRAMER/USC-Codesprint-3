n=int(input())
if 1<=n<=50:
    l=[]
    for i in range(n):
        row=[]
        a=input().split()
        for j in a:
            e=int(j)
            if -1000<=e<=1000:
                row.append(e)
            else:
                print("Value between -1000 and 1000")
        l.append(row)
    d1=0
    d2=0
    for i in range(n):
        d1=d1+l[i][i]
        d2=d2+l[i][n-i-1]
    if d1==d2:
        print("YES")
    else:
        print("NO")
else:
    print("Invalid Input")