n=int(input())
if 2<=n<=100:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if -100000<=e<=100000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        a1=l[0]
        a2=l[1]
        mini=abs(l[0]+l[1])
        for i in range(n):
            for j in range(i+1,n):
                s=abs(l[i]+l[j])
                if s<mini:
                    mini=s
                    a1=l[i]
                    a2=l[j]
        print(a1,a2)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")