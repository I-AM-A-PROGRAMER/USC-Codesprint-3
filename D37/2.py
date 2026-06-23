a=input().split()
n=int(a[0])
k=int(a[1])
if 1<=n<=100000 and -10000000<=k<=10000000:
    l=[]
    valid=True
    b=input().split()
    for i in b:
        e=int(i)
        if -1000<=e<=1000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        d={0:1}
        s=0
        ans=0
        for i in l:
            s=s+i
            if s-k in d:
                ans=ans+d[s-k]
            if s in d:
                d[s]=d[s]+1
            else:
                d[s]=1
        print(ans)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")