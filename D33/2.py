a=input().split()
n=int(a[0])
k=int(a[1])
if 1<=k<=n<=100000:
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
        d=[]
        front=0
        for i in range(n):
            while len(d)>front and d[front]<=i-k:
                front=front+1
            while len(d)>front and l[d[-1]]<=l[i]:
                d.pop()
            d.append(i)
            if i>=k-1:
                print(l[d[front]],end=" ")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")