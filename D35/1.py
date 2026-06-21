a=input().split()
n=int(a[0])
k=int(a[1])
if 1<=n<=100000 and 0<=k<=1000000000000000:
    l=[]
    valid=True
    b=input().split()
    for i in b:
        e=int(i)
        if 0<=e<=1000000000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        l.sort()
        s=0
        ans=0
        for i in range(n):
            if s>=k:
                ans=ans+1
            s=s+l[i]
        print(ans)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")