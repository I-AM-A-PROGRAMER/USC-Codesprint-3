n=int(input())
if 2<=n<=100000:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if 0<=e<=10000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        left=0
        right=n-1
        ans=0
        while left<right:
            area=min(l[left],l[right])*(right-left)
            if area>ans:
                ans=area
            if l[left]<l[right]:
                left=left+1
            else:
                right=right-1
        print(ans)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")