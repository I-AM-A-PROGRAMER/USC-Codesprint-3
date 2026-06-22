n=int(input())
if 1<=n<=100000:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if 0<=e<=1000:
            l.append(e)
        else:
            valid=False
    q=int(input())
    if 1<=q<=100000 and valid==True:
        l.sort(reverse=True)
        for i in range(q):
            x=int(input())
            left=0
            right=n-1
            pos=-1
            while left<=right:
                mid=(left+right)//2
                if l[mid]==x:
                    pos=mid
                    right=mid-1
                elif l[mid]<x:
                    right=mid-1
                else:
                    left=mid+1
            if pos==-1:
                print("No Rank")
            else:
                print("Rank",pos+1)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")