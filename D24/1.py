a=input().split()
n=int(a[0])
w=int(a[1])
if 1<=n<=100000 and 1<=w<=1000000000:
    l=[]
    valid=True
    b=input().split()
    for i in b:
        e=int(i)
        if 1<=e<=10000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        left=0
        s=0
        ans=0
        for right in range(n):
            s=s+l[right]
            while s>w:
                s=s-l[left]
                left=left+1
            if right-left+1>ans:
                ans=right-left+1
        print(ans)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")