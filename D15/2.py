n=int(input())
if 2<=n<=200000 and n%2==0:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if 1<=e<=1000000000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        l.sort()
        ans=0
        i=0
        j=n-1
        while i<j:
            s=l[i]+l[j]
            if s>ans:
                ans=s
            i=i+1
            j=j-1
        print(ans)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")