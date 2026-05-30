n=int(input())
if 1<=n<=100:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if 0<=e<=1000000000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        shf=0
        for i in range(1,n):
            key=l[i]
            j=i-1
            while j>=0 and l[j]>key:
                l[j+1]=l[j]
                shf=shf+1
                j=j-1
            l[j+1]=key
        for i in l:
            print(i,end=" ")
        print()
        print(shf)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")