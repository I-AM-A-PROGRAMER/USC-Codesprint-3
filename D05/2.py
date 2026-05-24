a=input().split()
n=int(a[0])
x=int(a[1])
if 1<=n<=100000 and 1<=x<=1000000000:
    l=[]
    b=input().split()
    for i in b:
        e=int(i)
        if 0<=e<=10000:
            l.append(e)
        else:
            print("enter between 0 and 10000")
    s=0
    ans=-1
    for i in range(n):
        s=s+l[i]
        if s>x:
            ans=i
            break
    print(ans)
else:
    print("Invalid Input")