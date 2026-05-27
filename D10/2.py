n=int(input())
if 1<=n<=100:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if -10000<=e<=10000:
            l.append(e)
        else:
            valid=False
    k=int(input())
    if -10000<=k<=10000 and valid==True:
        trip=False
        for i in range(n):
            for j in range(i+1,n):
                for m in range(j+1,n):
                    if l[i]+l[j]+l[m]==k:
                        trip=True
        if trip==True:
            print("YES")
        else:
            print("NO")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")