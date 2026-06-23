a=input().split()
n=int(a[0])
k=int(a[1])
if 1<=k<=n<=100000:
    l=[]
    valid=True
    b=input().split()
    for i in b:
        e=int(i)
        if 1<=e<=1000000000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        l.sort()
        for i in range(n-k,n):
            print(l[i],end=" ")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")