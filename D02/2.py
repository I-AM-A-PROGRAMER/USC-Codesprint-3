n=int(input())
if 2<=n<=100000:
    l=[]
    x=input().split()
    for i in x:
        e=int(i)
        if -10000<=e<=10000:
            l.append(e)
        else:
            print("Amt betwen -10^-4 nd 10^4 allow")
    m1=l[0]
    for i in l:
        if i>m1:
            m1=i
    m2=-10001
    for i in l:
        if i>m2 and i !=m1:
            m2=i
    print(m2)
else:
    print("n between 2 nd 10^5 allow")