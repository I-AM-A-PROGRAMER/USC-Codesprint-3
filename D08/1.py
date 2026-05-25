n=int(input())
if 1<=n<=100000:
    l=[]
    a=input().split()
    for i in a:
        e=int(i)
        if 0<=e<=1000000000:
            l.append(e)
        else:
            print("Invalid Input")
    for i in l:
        c=0
        while i>0:
            if i%2==1:
                c=c+1
            i=i//2
        if c%2==1:
            print("ANSWER")
        else:
            print("SAFE")
else:
    print("Invalid Input")