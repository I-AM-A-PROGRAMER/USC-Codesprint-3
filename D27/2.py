a=input().split()
n=int(a[0])
m=int(a[1])
if 1<=n*m<=100000:
    l=[]
    valid=True
    for i in range(n):
        b=input().split()
        row=[]
        for j in b:
            e=int(j)
            if -1000000000<=e<=1000000000:
                row.append(e)
            else:
                valid=False
        l.append(row)
    x=int(input())
    if valid==True:
        left=0
        right=n*m-1
        found=False
        while left<=right:
            mid=(left+right)//2
            r=mid//m
            c=mid%m
            if l[r][c]==x:
                found=True
                break
            elif l[r][c]<x:
                left=mid+1
            else:
                right=mid-1
        if found==True:
            print("FOUND")
        else:
            print("NOT FOUND")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")