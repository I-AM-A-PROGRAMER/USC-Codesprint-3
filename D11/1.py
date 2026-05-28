n=int(input())
if 1<=n<=100:
    l=[]
    valid=True
    a=input().split()
    for i in a:
        e=int(i)
        if e==0 or e==1 or e==2:
            l.append(e)
        else:
            valid=False
    if valid==True:
        l.sort()
        for i in l:
            print(i,end=" ")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")