a=input().split()
n=int(a[0])
x=int(a[1])
if 1<=n<=100000 and 1<=x<=1000000000:
    l=[]
    valid=True
    b=input().split()
    for i in b:
        e=int(i)
        if 1<=e<=1000000000:
            l.append(e)
        else:
            valid=False
    if valid==True:
        s=set(l)
        used=set()
        ans=0
        for i in s:
            y=x-i
            if y in s and (y,i) not in used:
                if i<y:
                    ans=ans+1
                    used.add((i,y))
                elif i==y:
                    c=0
                    for j in l:
                        if j==i:
                            c=c+1
                    if c>=2:
                        ans=ans+1
                        used.add((i,i))
        print(ans)
    else:
        print("Invalid Input")
else:
    print("Invalid Input")