n=int(input())
if 3<=n<=100000:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if 1<=e<=1000000000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        left=0
        right=n-1
        while left<=right:
            mid=(left+right)//2
            if l[mid]>l[mid-1] and l[mid]>l[mid+1]:
                print(l[mid])
                break
            elif l[mid]<l[mid+1]:
                left=mid+1
            else:
                right=mid-1
    else:
        print("Invalid Input")
else:
    print("Invalid Input")