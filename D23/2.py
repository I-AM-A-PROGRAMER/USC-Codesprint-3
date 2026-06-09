n=int(input())
if 1<=n<=100:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if 1<=e<=1000000:
            l.append(e)
        else:
            valid=False
    q=int(input())
    if 1<=q<=100 and valid==True:
        for i in range(q):
            a=input().split()
            left=int(a[0])
            right=int(a[1])
            if 0<=left<=right<n:
                d={}
                for j in range(left,right+1):
                    if l[j] in d:
                        d[l[j]]=d[l[j]]+1
                    else:
                        d[l[j]]=1
                ans=0
                for j in d:
                    ans=ans+d[j]*d[j]
                print(ans)
            else:
                print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")