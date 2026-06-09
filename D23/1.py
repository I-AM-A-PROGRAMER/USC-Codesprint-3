n=int(input())
if 1<=n<=100:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if -1000000000<=e<=1000000000:
            l.append(e)
        else:
            valid=False
    q=int(input())
    if 1<=q<=100000 and valid==True:
        for i in range(q):
            a=input().split()
            left=int(a[0])
            right=int(a[1])
            if 0<=left<=right<n:
                maxi=l[left]
                mini=l[left]
                for j in range(left,right+1):
                    if l[j]>maxi:
                        maxi=l[j]
                    if l[j]<mini:
                        mini=l[j]
                print(maxi-mini)
            else:
                print("Invalid Input")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")