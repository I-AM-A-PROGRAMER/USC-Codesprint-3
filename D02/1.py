n=int(input())
if 1<=n<=100000:
    l=[]
    t=0
    for i in range(n):
        e=int(input())
        if 0<=e<=100:
            l.append(e)
            t=t+e
        else:
            print("score between 0 and 100 allow")
    avg=t/n
    c=0
    for i in l:
        if i>avg:
            c=c+1
    print(c)
else:
    print("n between 1 and 10^5 allow")