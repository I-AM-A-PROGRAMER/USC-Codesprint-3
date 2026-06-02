a=input().split()
n=int(a[0])
k=int(a[1])
x=int(a[2])
if 1<=n<=100000 and 1<=k<=n and 1<=x<=1000000000:
    l=[]
    valid=True
    b=input().split()
    for i in b:
        e=int(i)
        if 0<=e<=10000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        found=False
        for i in range(n-k+1):
            s=0
            ok=True
            for j in range(i,i+k):
                s=s+l[j]
                if l[j]==0:
                    ok=False
            if s>=x and ok==True:
                found=True
        if found==True:
            print("YES")
        else:
            print("NO")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")