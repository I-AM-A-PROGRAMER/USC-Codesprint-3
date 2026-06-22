n=int(input())
if 1<=n<=100000 and n%2==1:
    l=[]
    valid=True
    a=input().split()
    x=0
    for i in a:
        e=int(i)
        if 1<=e<=100:
            l.append(e)
            x=x^e
        else:
            valid=False
    if valid==True:
        l.sort()
        pos=0
        for i in range(n):
            if l[i]==x:
                pos=i+1
                break
        print(x,pos)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")